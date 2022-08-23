from django.apps import AppConfig

#이게 config/settins.py 파일의 INSTALLED_APPS 항목에 추가되지 않으면 장고는 pybo 앱을 인식하지 못한다.
class PyboConfig(AppConfig): #pybo 앱을 만들 때 자동으로 생성된 것.
    name = 'pybo'
