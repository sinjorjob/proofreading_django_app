from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.staticfiles.templatetags.staticfiles import static
from . import forms
from django.template.context_processors import csrf
from . import apido


message = '''■誤字脱字の定義<br>
        <b>Proofreading APIで指摘されるもの。</b><br>
        漢字変換間違い：読みは正しいが漢字が違う。<br>
        助詞間違い：助詞の用法が違う、または、不要な助詞が入っている。<br>
        文法間違い： 漢字・助詞間違いに該当しないもの。脱字。助詞以外の不自然な文字が挿入されているもの。<br>
        その他、１〜数文字が間違っている文章。<br>
        <b>Proofreading APIで指摘されないもの。</b><br>
        ◆敬語の使い方間違い。<br>
        ◆体言どめを止めたほうがいいケース。<br>
        ◆ひらがなより漢字のほうが適切なケース。<br>
        ◆句点を追加した方がいいケース。<br>
        ◆意味は通じるがより美しい日本語が有るようなケース。<br>
        ◆そもそも文が日本語として破綻しており、誤字脱字のレベルでないもの。'''

def demo(request):
    api = apido.Apido()
    if request.method == 'POST':
        # テキストボックスに入力されたメッセージ
        textone = request.POST["textone"]
        sensitivity = request.POST["sensitivity"]
        # APIリクエストを投げてからの応答を取得
        rets,suggestions = api.get(textone,sensitivity)
        form = forms.UserForm(initial={'textone' : textone})
        
        c = {
             'form': form,
             'textone':textone,
             'message':message,
             'rets':rets,
             'suggestions':suggestions
        }
    else:
        # 初期表示の時にセッションもクリアする
        request.session.clear()
        # フォームの初期化
        form = forms.UserForm(label_suffix='：')

        c = {'form': form,
             'message':message
        }
    c.update(csrf(request))
    return render(request,'app/demo.html',c)