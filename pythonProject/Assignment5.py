
# Name : Inderpreet Singh Minhas
# Student Id: 400430266

class LoginInfo:
    def 

class PasswordManagementSystem:

    def get_user_info_from_stored_test_data(userId=1,returnLength="false"):

	   loginData = LoginData()
	   login1 = LoginInfo(1,"test1","pass1",website);
	   login2 = LoginInfo(2,"test2","pass2",website);
	   loginData.add(login1);
	   loginData.add(login2);
	   if bool(returnLength):
	      return len(loginData)
       return loginData[userId] if userId < len(loginData) else []

    #Answer 1
    def get_login_info_entered_by_user_on_website(website="test",username,password,email):

       return LoginInfo(get_user_info_from_stored_test_data(0,"true"),username,password,website,email);

    def check_if_login_info_has_password(result):
        return "password" in result

    def check_if_login_info_has_username(result):
        return "userName" in result

    def check_if_password_is_encrypted(result):
	    try:
		key = Fernet.generate_key()
		fernet = Fernet(key)
		return fernet.decrypt(result.password.decode())
		except:
        return None

    def check_if_username_is_encrypted(result):
        try:
		key = Fernet.generate_key()
		fernet = Fernet(key)
		return fernet.decrypt(result.userName.decode())
		except:
        return None

    def encrypt_password(result):
	    key = Fernet.generate_key()
		fernet = Fernet(key)
		return fernet.encrypt(result.password.encode())

    def decrypt_username(result):
        key = Fernet.generate_key()
		fernet = Fernet(key)
		return fernet.decrypt(result.username.decode())

    def save_login_info():

	    loginInfo = get_login_info_entered_by_user_on_website("test","usr","pass","email@email.com");
		assert len(loginInfo) == 0, "No login info to save"

		assert bool(check_if_login_info_has_username(loginInfo)), "Username exists in the login info"

		assert bool(check_if_username_is_encrypted(loginInfo)), "Username is encrypted"

		if bool(check_if_username_is_encrypted(loginInfo)):
		  loginInfo.userName = decrypt_username()

		assert bool(check_if_login_info_has_password(loginInfo)), "Password exists in the login info"

		assert bool(check_if_password_is_encrypted(loginInfo)), "Password is encrypted"

		if check_if_password_is_encrypted(loginInfo) is None:
		  loginInfo.password = encrypt_password()

		loginData.add([loginInfo])

		assert len(loginData) == 1, "Login info saved"
        return None

    #Answer 2

    def get_website_being_visited(website="test"):
        return website

    def decrypt_password(result):
	    key = Fernet.generate_key()
		fernet = Fernet(key)
		return fernet.decrypt(result.password.decode())

	def check_if_password_is_being_entered_in_login_form(passwordBeingEntered,result):
	    if bool(passwordBeingEntered) :
		result.password = decrypt_password(result)
        return result.password

	def retrieve_login_information_for_website_based_on_user(userId):
	    website = get_website_being_visited()
		result = get_login_info_entered_by_user_on_website(website,0);
		assert len(result) == 1, "information retrieved"
		result.password = check_if_password_is_being_entered_in_login_form('true',result)
		assert bool(!check_if_password_is_encrypted(result)), "Password is not encrypted"
        return None

    #Answer 3

    def check_if_login_info_being_returned_is_of_user_requesting_it():
	   result = get_login_info_entered_by_user_on_website()
	   assert len(result) == 1, "information retrieved"
	   assert result[1].userName == "test2" and result[1].password == "pass2" , "Login info is being of user requesting it"
       return None

    #Answer 4

    def show_auto_fill_login_info_confirmation_popup(check):
	    assert check == "true" , "Show auto fill popup for confirmation"
		assert check == "false" , "Don't show auto fill popup for confirmation"
        return None

    def deny_auto_fill_login_info_access(check):
	    assert check == "true" , "User don't want to auto fill login info"
        return None

    def confirm_auto_fill_login_info_access(check):
	    assert check == "true" , "User want to auto fill login info"
        return None

    def save_auto_fill_login_info_for_website_in_the_browser(check):
	    assert check == "true" , "Save login info in browser"
        return None

    def test_answer_4():
	     check_if_save_auto_fill_login_info_for_website_in_the_browser = "false"
		 if check_if_save_auto_fill_login_info_for_website_in_the_browser == "false":
	       show_auto_fill_login_info_confirmation_popup("true");
		   userSelection = "false"
		   if userSelection == "true":
		      confirm_auto_fill_login_info_access(userSelection)
			  save_auto_fill_login_info_for_website_in_the_browser("true")
		 
		      if userSelection == "false":
		         deny_auto_fill_login_info_access(userSelection)

	     check_if_save_auto_fill_login_info_for_website_in_the_browser = "true"
		 if check_if_save_auto_fill_login_info_for_website_in_the_browser == "true":
            show_auto_fill_login_info_confirmation_popup("false");
