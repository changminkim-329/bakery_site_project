from django import forms
from .models import User
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=128,label="이메일",
                            error_messages={'required':"이메일을 입력해주세요."})
    password = forms.CharField(max_length=256, widget=forms.PasswordInput, label="비밀번호",
                error_messages={'required':'비밀번호를 입력해주세요.'}
    )

    def clean(self):
        clean_data = super().clean()
        
        email = clean_data.get('email')
        password = clean_data.get('password')

        if(email != None):
            if(password != None):
                try:
                    user_object = User.objects.get(email=email)

                    if(user_object.password != password):
                        self.add_error('password','비밀번호가 틀립니다.')

                except Exception as e:
                    self.add_error('password','해당 계정이 없습니다.')
                    print(e)

            else:
                self.add_error('password','비밀번호를 입력해주세요.')
        
        else:
            self.add_error('email','이메일을 입력해주세요.')



class UserEditForm(forms.Form):
    GENDER_CHOICE = (
        ('M','남자'),
        ('F','여자'),
        ('etc','그 이외')
    )

    username = forms.CharField(max_length=128, label="사용자이름",
                            error_messages={'required':"이름을 입력해주세요."})

    password = forms.CharField(max_length=256, widget=forms.PasswordInput, label="비밀번호",
                error_messages={'required':'비밀번호를 입력해주세요.'})

    re_password = forms.CharField(max_length=256, widget=forms.PasswordInput, label="비밀번호 확인",
                error_messages={'required':'비밀번호를 입력해주세요.'})

    gender = forms.ChoiceField(label="성별", choices=GENDER_CHOICE)

    contact_number = forms.CharField(max_length=50, label="연락처",
                            error_messages={'required':"연락처를 입력해주세요."})

    address = forms.CharField(max_length=256, label="주소",
                            error_messages={'required':"주소를 입력해주세요."})


    def clean(self):
        clean_data =  super().clean()

        username = clean_data.get('username')
        password = clean_data.get('password')
        re_password = clean_data.get('re_password')
        gender = clean_data.get('gender')
        contact_number = clean_data.get('contact_number')
        address = clean_data.get('address')

        if (password != re_password):
            self.add_error('re_password','비밀번호가 다릅니다.')
        

