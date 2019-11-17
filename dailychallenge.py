#DAILY CHALLENGE


first_name = input("Enter your FIRST name:")
last_name = input("Enter your LAST name:")
education = input ("Do you have a degree? Please specify:")
prev_position = input ("What was your previous working place?")
experience = input("How long did you work there?")
char = input("Write about your biggest professional achivement from last 2 years:")


html_cv = f'''
<!DOCTYPE html>
<html>
<head>
	<title>CV</title>
</head>
<body>
	<h1> Name: {first_name.capitalize()} {last_name.capitalize()} </h1>
	<h3> Education: {education} </h3>
	<h3> Previous position was {prev_position} with experience of {experience} years. </h3>
	<h5> The biggest goal achived at previous position: {char}. </h5>
</body>
</html>
'''
print(html_cv)

