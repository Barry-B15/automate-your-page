
header = '''
<!-- The header is not going to change much for now, so it is manual -->
<!DOCTYPE html>
	<!-- This is the beginning of my html -->
<head>
	<title>Okori: NDIP Baby Step Notes</title>
	<link rel="stylesheet" type="text/css" href="css/mystyle3.css">
</head>
<body>
	<h1><!-- Always Edit Header Title To fit the Stage! --> ND Stage 2 </h1>
	<div class="lesson"> <!-- opening div for lesson --> '''


footer = '''
<!-- This is the ending html, also not changing much so it is manual -->
	</div> <!-- This is the lesson div ending -->
</body> <!-- This is the body ending -->
</html> <!-- This is the end of the page html --> '''


#def generate_concept_HTML(concept_title, concept_description):
	html_text_1 = '''
	<div class="concept">
		<div class="concept_title">
			''' + concept_title
	html_text_2 = '''
		</div>
		<div class="concept_description">
			''' + concept_description
	html_text_3 = '''
		</div>
	</div>'''
	full_html_text = html_text_1 + html_text_2 +html_text_3
	return full_html_text

def generate_concept_HTML(concept_title, concept_description):
	html_text_1 = '''
	<div class="concept" id="lesson-1.1"> <!-- May have to manually change lesson id -->
		<div class="concept_title">
			''' + str(concept_title) #adjust for str
	html_text_2 = '''
		</div>
		<div class="concept_description">
			''' + str(concept_description) #adjust for str
	html_text_3 = '''
		</div>
	</div>'''
	full_html_text = html_text_1 + html_text_2 +html_text_3
	return full_html_text

def baby_1step_HTML(concept):
        #This defines our concept title and concept description, generates html for single concept
	concept_title = concept[0]
	concept_description = concept[1]
	return generate_concept_HTML(concept_title, concept_description)

def my_baby_steps_HTML(list_of_concepts):
        #This is the code to generate many concepts
	HTML = ""
	for concept in list_of_concepts:
		concept_HTML = baby_1step_HTML(concept)
		HTML = HTML + concept_HTML
	return HTML

def TEST_many_baby_steps_HTML(list_of_concepts):
	HTML = ""
	for concept in list_of_concepts:
		concept_HTML = baby_1step_HTML(concept)
		HTML = HTML + concept_HTML
	return "HTML PASSED" #For test cases

#The following code takes a lesson as input, adds the header and footer defined
#earlier and returns a page with lesson, header and footer as output.
def generate_my_page_HTML(concept_list):
	all_html = ''
	for concept in concept_list:
		concept = baby_1step_HTML(concept)
		all_html = all_html + concept
	return header + all_html + footer


#I'm also tried to generate list for my Table of Content with the following
#Lists

def generate_ul_HTML_open(concept): #opening ul
	html_text_1 = '''
	<div class="concept">
		<ul class="concept_title">
			'''
	full_html_text = html_text_1
	return full_html_text


def generate_ul_HTML_close(concept): #for the closing ul
	html_text_1 = '''
		</ul>
	</div> '''
	full_html_text = html_text_1 
	return full_html_text


def generate_list_items(concept): #for the list items
	html_text_1 = '''
		<li><a href="#lesson-0.0"> <!-- Insert lesson id manually -->
			'''  + str(concept)
	html_text_2 = '''
		</a></li> '''
	full_html_text = html_text_1 + html_text_2
	return full_html_text
	    
def generate_all_my_HTML(concept_list):
	all_html = ''
	for concept in concept_list:
		concept = generate_list_items(concept)
		all_html = all_html + concept
	return all_html

#The following code takes the opening and closing list tags above, wrap the around the list items and return an un-ordered list
#There may be a better way but I'm still learning how to improve that.
    
def generate_all_list_html(concept_list):
	return generate_ul_HTML_open(concept_list) +'' +generate_all_my_HTML(concept_list) + generate_ul_HTML_close(concept_list)

    
