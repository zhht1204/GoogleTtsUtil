import sys
import urllib.request
import os.path

def save_voice_file(voice_text):
	url='https://translate.google.com/translate_tts?q={voice_text}&tl=zh-CN&client=tw-ob'
	headers={
		'Referer': 'http://translate.google.com/',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
	}
	voice_text_quote = urllib.request.quote(voice_text)
	url = url.format(voice_text=voice_text_quote, tk=622310.1043180)
	request = urllib.request.Request(url, headers=headers)
	response = urllib.request.urlopen(request).read()
	# print(response)
	# save file
	saved_file = open(os.path.join('export','voice.mp3'), 'wb')
	saved_file.write(response)
	saved_file.close()

if __name__ == '__main__':
	if len(sys.argv) > 1:
		voice_text = sys.argv[1]
		save_voice_file(voice_text)
	else:
		print('请输入要转换的句子')

