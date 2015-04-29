
Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information. 

#Lesson1: Introduction
#Run program here to generate html

stage1_lesson1 = [['Getting Started', 'Nanodegree is a <b>Path</b>, from Nothing to gaining new knowledge and new skills, to learning new ways of thinking.<br>After this program,<b> we could choose to specialize in</b>: Full stack programming, Frontend Web Development, ios development or something else. <br><br>\
<h3>Coding</h3>\
<br><br>Coding a computer means telling the computer what you want it to do, by writing text in a way the computer understands'],
 ['Five steps to Thinking like a Programmer', 'Computer programmers follow a systematic way of thinking and approaching computer programs. They take five different steps: <br><br>\
1. Procedural Thinking: Step by step approach to program design and creation, using clear instructions that the computer understand.<br>\
2. Abstract Thinking: Using abstract thinking like: 1+1 = 2 and finding similarities(generality) amongst seemingly different things.<br>\
3. Technological Empathy: Knowing how the computer sees things and using that to write instructions like: I am bold, taking special note that the computer is stupid and that any little mistake could cause big problems.\
<br> 4. Systems Thinking: Take a big idea and break it down into component pieces.\
<br>5. Systematic debugging: - Look at a program problem, think of possible causes and find a way to fix it.'],
 ['How The Web Works', 'The Web is a collection of computers that communicate with each other. When we type a request on our BROWSERS to a WEB PAGE, the web page send our requests through the INTERNET using the HTTP protocol to the SERVER. The server then sends the requested file or document to our browsers through the internet. Web documents may be plain text, html, images, video or music files.'],
 ['Components of the Web', 'HTML The web is made up of HTML pages. HTML stands for Hypertext Markup Language. They form majority of the contents on the web today. HTML components are text contents - the contents we see on a web page and markup - which tells the computer how to render the content (we usually do not see this part).<br>\
URL Stands for Univeral Resource Locator. They are the links on a website or the web addresses linked from web pages. For example, the link to Udacity Homepage\
<br>HTTP Is short for Hypertext Transfer Protocol, the foundation and protocol that unite the web.\
<br>Web Applications And of course web applications.'],
 ['Basic HTML Vocabulary', 'Tag: An html tag is always contained in angled brackets, an opening &lt; &gt; and closing &lt;/ &gt; tags.\
<br>Void tags like "break" - &lt;br &gt; and "image" - &lt;img &gt; have no closing tag\
<br>An html Element refer to everything between the opening and closing tags and the Attribute refers to the property of the element.\
<br>HTML could be either inline which posts inline or block which creates an invisible block around contents.\
<br>Examples of inline elements are the  "&lt;break&gt;" , "&lt;em&gt;", "&lt;img&gt;", "&lt;span&gt;". While the "&lt;p&gt;", "&lt;div&gt;", "&lt;form&gt;" \
are "block" elements.<br>HTML controls the structure of a webpage. They are like the walls of a house.']]
 

#Lesson2: Creating a Structured Document with HTML
#Run program here to generate html
stage1_lesson2 = [['HTML Structure', 'HTML is structured like the branches of a tree. Developers and programmers refer to this tree-like structure as DOM -"Document Object Mode". This tree-like structure can be likened to a family tree starting from children to parents, to grand-parents up to ancestors. The HTML structure can also be compared to a house with a sitting-room leading to other rooms.'],
['Relationship between indented HTML and boxes', 'Everything on a page is a box. And the boxes are nested. When we read HTML as documents, for example in Developer tools, we see a wave of changing indentations down from left to right. This shows the position of the box as related to others. The indented an element is, the more deeply nested its corresponding box.'],
['Text Editors', 'There are many types of text editors. Examples are Scratchpad, Codepen, Sublime, Notepad to mention a few. It is recommended we do not use Notepad as they are not designed for coding for computers. We are recommended to use Scratchpad to write HTML and CSS, then copy and paste in Codepen to share. Use Sublime to write and save on computers.\
<br><br>Scratchpad: Good for beginners, supports two languages but impossible for sharing\
<br>Codepen: Not very beginner friendly, supports three languages and very professionalism but requires an account\
<br>Sublime: Is difficult for beginners but its highest rated for professional works and supports all languages.'],
['Developer Tools', 'Developer tools are available in browsers. They provide a great way for us to test our codes,resize the boxes and try new colors and fonts without changing our codes until we find something satisfactory.']]
 

#Lesson3: Adding CSS Style to HTML Structure
#Run program here to generate html
stage1_lesson3 = [['CSS', 'CSS - Cascading Style Sheet is used to control and style our pages. It is comparable to the paints on our walls or the furniture in our homes. So we build the structures of our pages with HTML and style them using CSS. It allows us to use specific syntax and rules to change how elements look on the page. With CSS, we can control font-sizes, colors, background, border and positions of things on our pages. For example; we can use CSS to style all &lt;h1&gt; on our page to MAROON'],
['Inheritance', 'In CSS, the most specific rule is applied to every element. Thats called Cascading. We go down and down the into the rule until we find the one that best describe the elements and that gets applied. This method is called Inheritance.\
<br>According to wikipedia:\
<br>Inheritance is a key feature in CSS, it relies on the ancestor-descendant relationship to operate. Inheritance is the mechanism by which properties are applied not only to a specified element, but also to its descendants.[11] Inheritance relies on the document tree, which is the hierarchy of (X)HTML elements in a page based on nesting. Descendant elements may inherit CSS property values from any ancestor element enclosing them. In general, descendant elements inherit text-related properties, but box-related properties are not inherited.\
<br>Properties that can be inherited are color, font, letter-spacing, line-height, list-style, text-align text-indent, text-transform, visibility, white-space and word-spacing.\
<br>Properties that cannot be inherited are background, border, display, float and clear, height and width, margin, min- and max-height and -width, outline, overflow, padding, position, text-decoration, vertical-align and z-index. Inheritance prevents certain properties from being declared over and over again in a style sheet, allowing the software developers to write less CSS. It enhances faster-loading of web pages by users and enables the clients to save money on bandwidth and development costs. <br>We can find documentation for fonts at MDN CSS-Fonts.'],
['Selector', 'A Selector defines what elements of a page a particular style will apply to. For example div followed by two {} braces will select the elements of the div, between the braces. The code is "selector { property: value;}"\
<br>h1 {\
<br>    color: yellow;\
<br>}\
tells the browser to make the color of h1, yellow.\
<br>To select a particular div, we use the Class Selector property value.<br> For example; &lt;div class="navigation"&gt;, we write\
<br>.navigation {\
<br>       color: red;\
<br>}'],
['Boxing', 'There are four main points that Jessica address about box sizing.<br><br>\
1. HTML elements are boxes and each box has 4 components.\
<br>2. Because there are so many components to each box, it can often be hard to get the size of a box just right.\
<br>3. There are two techniques you can use to help deal with sizing issues.\
<br>i. Set sizes in terms of percents rather than pixels.\
<br>ii. Set the box-sizing attribute to border-box for every element.\
<br>4. Different browsers work slightly differently. Sometimes this causes different browsers to display the same code differently<br><br>\
Box Positioning<br><br>\
By default, block elements like divs take up the entire with of the page<br>\
To display several elements next to each other we add display: flex; to the mother div or container']]

#Important Design Hints
#Generate HTML

stage1_design_hints = [['Hint 1', '1. Look for natural boxes<br>\
2. Look for repeated styles and semantic elements\
3. Write your HTML\
4. Apply styles from the biggest site-wide elements to the smallest\
5. Test design on other browsers, resize windows, and fix things using steps 3 and 4 above\
6. Use google developers tools to test colors, font, sizes on the fly without changing codes unless necessary.']]



stage2_lesson1 = [[ 'Computer', 'A universal machine that can do whatever we want it to do. But pretty useless without a program'],
	['Computer Program', 'A set of instructions that tell a computer what to do'],
	['Programming Language', 'A language the computer understands, examples are COBOL, Python, C++ etc'],
	['Python', 'Is a higher-level language used to write programs. It is called an <b>Interpreter</b> which means it can run,\
            interpret and execute the programs that we write in Python language '], 
	['Grammer', 'Python is very strict on grammar. No mistake is acceptable, codes must match language grammar exactly.'],
	['Python Expressions', "They are similar to Arithmetic expressions '+', '*' etc. 2 + 2, (2 * (3 + 5) + 7)"],
	['Computation', "A '<b>'Cycle'</b>'  is the time it takes a computer to do one step. A computer does 2.7 billion cycles(2.7GHz) per second"],
        ['Reflection', 'Helps you bridge the knowledge gap between how novices and experts handle materials']]

stage2_lesson2 = [['Variables', 'In Python, a variable is a way of giving a <span class="bold">name</span> to some <span class="bold">value</span>.<br>\
          Written as <span class="code">Name = Expression</span> <br>where name can be any sequence of letters, or letters and numbers as well as underscores.\
          The value of a name is the value that it refers to.\
          Once we have defined that variable we can change the value. And when we use the name again, it refer to the new value.\
          For example;<br> sum3 = 3 + 3 <br> sum3 = sum3 + 3 <br> Output 9(not 6)'],
	 ['To assign a value to a variable', '<p>This means to give the variable ususally on the left, a value - on the right of something like an equal sign\
	  in the middle</p><p><span class="code">name = Expression</span><br>\
	  The convention is to write variables in lowercase letters <br>\
	  <span class="code">my_city = Port Harcourt</span><br> \
	  The variable my_city is assigned the value, Port Harcourt.</p>'
	     '''<p>
		  We can change the value later like <br>
		  <span class="code">my_city = Tokyo</span>
		</p>'''],
	 ['The difference between the equal signs in <span class="code">2 + 3 = 5</span> and <span class="code">my_variable = 5</span>',
	  '''<p>
		  The line <span class="code">2 + 3 = 5</span>, means, when you add the numbers 2 and 3 you get 5. That is, the numbers on both side of\
		  the equal sign are <span class="bold">"the same"</span>.
	     </p>
             <p>
		  But in the line <span class="code">my_variable = 5</span>, the equals sign means <span class="bold">"we are assgning the value 5 to the\
		  variable, my_variable"</span>.
	     </p>'''],
         ['Usefulness of variables',\
	  '''<p>
		  Variables can be useful to programmers in many ways:
            </p>
        <ul>
          <li>They improve code readability by using names that make sense to humans.</li>
          <li>They give us a way to store the value of important data.
          </li>
          <li>They provide a way for us to use stored values</li>
          <li>They give us a way to change the value of something (like in the line <span class="code">days = days-1</span></li>
        </ul>'''],
        ['The difference between <span class="code">2 + 2</span> and\
		<span class="code">"2" + "2"</span>', '''
		<p>
		  The code <span class="code">2 + 2</span> would add the numbers to give <span class="code">4</span>.
		</p>
		<p>
		  And the code <span class="bold">"2" + "2"</span> would paste the two strings together to give a new string\
		  <span class="code">"22"</span>. This way of using the\
		  <span class="bold">+</span> sign to join two strings\
		  together is called <span class="bold">concatenetion</span> of two strings
		  <span class="code">&lt;string&gt; + &lt;string&gt;</span> \
		</p>'''],
	['The Need for Carefulness',
	'''<p>
		A <span class="bold">String</span> is a sequence of characters \
		  surrounded by <span class="bold">quotes</span>. Quotes could be \
		  single <span class="code">'</span> or double <span class="code">"\
		  </span> but <span class="bold">must close</span> with the same type \
		  of quotes.
	</p>
        <p>
          <span class="code">
            'Hello, I am single'<br>
            'Hi! I am single, too'<br>
            "Wow, now we are a pair"<br>
            "Great! And now I see everything double."</span>
        </p>
		Python will give us an error message for the following:
        <p>
          <span class="code">'George"</span>, <span class="code">"Dave'</span>, <span class="code">"Game"'</span>, <span class="code">'Boy</span>,\
          <span class="code">Python"</span>, <span class="code">Elvis</span>
        </p>''']]

stage2_lesson3 = [['What is a <span class="bold">function or procedure</span>?', 'A function(or procedure) is a part of a\
            program that takes <span class="bold">inputs</span>, process them and produce some\
            <span class="bold">outputs</span> or modify some parameter(s).<br> A general form is:"]<br><br>\
            <span class="code"> &lt;function&gt;(&lt;input&gt;, &lt;input&gt;, &lt;input&gt; ......)</span> <br><br>\
            Inputs are also called <span class="bold">operands</span>, <span class="bold">arguments</span> or\
            <span class="bold">parameters</span>. The number of outputs and inputs must match.' ],
         ['The difference between making and using a function', 'To make a function, line1 starts with the keyword\
            <span class="code">def</span>, followed by a space, then function name, followed by the function parameters\
            enclosed in parentheses. These parameters are given actual values when used(or called). Line1 ends with colons \
            after the closing parentheses. Line2 starts with indentation,  then the body of the function, that is the code\
            that specifies what the function does with the input parameter(s).<br><br><span class="code">\
            def my_name(first_name, last_name): <br> &nbsp; &nbsp; &nbsp; full_name = first_name + ' ' + last_name <br>\
            &nbsp; &nbsp; &nbsp; return full_name </span>. <br><br> <span class="bold">To use a function</span>,\
            we write the name of the function,  give actual values to the parameters in parentheses.<br>For example; the above\
            function with first_name(John) and last_name(Doe), we write:<br><br>\
            <span class="code"> print my_name ("John", "Doe")</span> <br><br> \
        				Will output: John Doe'],
        ['How useful are functions to programmers?', 'Functions are great tools for taking care of repetitive tasks. They free us from \
            having to go through repeating the same thing over and over again. It would be very difficult and even boring for a programmer \
            to teach a computer for example, how to convert fahrenheit to celsius everytime he wants to use it in his program before using it. \
            But with a simple function, all he needs to do is call the function.'],
        ["What happens if a function doesn't have a return statement?", 'The return statement in a function is what tells Python what to output. \
            So if we were to write a function without a return statement; when we print, Python will output <span class="code">None</span>'],
    ['Using Functions to Generate HTML', 'Programmers use functions to generate HTML codes for web pages. It helps them avoid repetition \
            and save time writing ccodes for very big projects.<br>\
            The attached function <span class="code"> def generate_concept_HTML(concept_title, concept_description)</span> (by ANDY)\
              will generate a simple HTML codes that we can copy to our webpage.' ]]

stage2_lesson4 = [['The (if) Statement', '<span class="bold">if statements</span> are used in decision making.<br>\
              It compare values and return the boolean values: <span class="bold">True</span> or <span class="bold">False</span>.\
              In comparisons, we use (==) for equality.<br>\
              The following function takes one argument and return "True" if the input is 16 or "False" as\
              output if the value is not 16. <br><br> <span class="code">\
                def age(x):<br>\
                  &nbsp;&nbsp;if x == 16:<br>\
                      &nbsp;&nbsp;&nbsp;&nbsp;return "True"<br>\
                  &nbsp;&nbsp;else:<br>\
                      &nbsp;&nbsp;&nbsp;&nbsp;return "False"\
                    </span>'],
    ['The "While" Loop', 'Like (if statements); the <span class="bold">While loop</span>, tests if the test expression is "True" or "False". <br>\
              It stops execution if the test expression is False on first trial. But will keep executing the body of the funtion as long as \
              the the "test codition" remains "True" until the test expression turns "False".\
              <br>The following program will print out numbers from 1,2,3,,,,,, 10 then stop.<br><br>\
              <span class="code">\
              i = 1 <br>\
              while i != 10:<br>\
                  &nbsp;&nbsp;i = i + 1<br>\
                  &nbsp;&nbsp;print i\
                </span> '],
    ['Lists', 'A <span class="bold">List</span> is a sequence of anything; charcaters, numbers or whatever we decide to include in the square bracket.<br> \
    We can build our lists and store very complex data structures in them.\
              <br>The general expression is:<br><br>\
                <span class="code"> \
                  <span class="blue">&lt;list&gt;</span> -> \
                  [<span class="blue">&lt;Expression&gt;</span>, \
                  <span class="blue">&lt;Expression&gt;</span>, ...] \
                </span>\
                <br><br>\
                A list can take any number of elements:\
              could be <span class="bold">empty [ ],  single [6]</span> or many [1,2,3,3,4,5,......].\
              <br> <br><span class="code">fruits = ["apple", "grape", "mango", "orange"]</span><br><br>\
              <span class="bold">Note: A List is ordered; meaning we have to arrange the list as given, separated by commas</span> <br><br>\
              <span class="bold">Nested Lists</span><br><br>\
              A list is nested when it is contained inside another list: <br><br>\
              <span class="code">mixed_up = [["apple", 5, "mangoes", 7, [1,2,["alpha", "beta"]]] </span> <br><br>\
              	We can use the lists to organize our work like in the following example <br><br>\
              	<span class="code">\
              	definitions = [ ["String", "A string is a sequence of characters"], <br>\
              ["List", "A list is a sequence of anything"], <br>\
              ["While Loop", "A while loop will continue to execute the body until the test expression is no longer true"]] </span> \
              <br><br>\
              Output: <br>\
              <span class="code">\
                print definitions[1] <br>\
                ["List", "A list is a sequence of anything"] <br>\
                >>> print definitions[2] <br>\
                ["While Loop", "A while loop will continue to execute the body until the test expression is no longer true"]<br>\
                >>> print definitions[0] <br>\
                ["String", "A string is a sequence of characters"]\
              </span>'],
    ['List Mutation And Aliasing', '<span class="bold">Mutation</span> modifies the value of a list after its been created. <br><br>\
    <span class="code">\
                p = [0,1,2,3,4,5] <br>\
                p[0] = "numbers" <br>\
                <br>print p<br>\
                >>> ["numbers", 1, 2, 3, 4, 5]\
              </span> <br><br>\
         When we refer to an object or list using another name, it is called <span class="bold">Aliasing</span>. This is very similar to a real \
         world "nickname" or the movie Spy "James Bond" alias "007".<br>\
              <span class="code"> spy = [0,0,7] <br> agent = spy <br>\
                print spy <br>\
                >>> [0, 0, 7] <br>\
                print agent <br>\
                >>> [0,0,7] </span><br>\
                 It is important to note that any change to one will also affect the other <br><br>\
                 <span class="code"> agent[2] = agent[2] + 1<br>\
                print spy <br>\
                >>> [0, 0, 8] <br>\
                print agent <br>\
                >>> [0,0,8]\
              </span>'],
    ['Debugging', '<span>Debugging</span> is a very important skill needed by software engineers to succeed in writing reliable software. \
        It is a scientific process of examining codes to discover unexpected bugs that can ruin a program.<br>\
          Five basic approach to debugging are:<br><br>\
           <ol>\
              <li>Examine error messages when programs crash <p>The last line of Python Tracebacks will tell you what went wrong. \
              Reading backwards from there will tell you more about where the problem occurred.</p></li>\
              <li>Work from example code <p> If your modified code does not work, comment it out and do step-by-step modifications to the example\
              code until it does what you want.</p></li>\
              <li>Make sure examples work <p> Just because you find example code does not mean it will work in your system. Check the example code\
              you are using to make sure it behaves the way you expect. </p></li>\
              <li>Check (print) intermediate results <p>When your code  does not crash, but does not behave as expected, add print statements to your\
              program to see where in the code things stop behaving correctly.</p></li>\
              <li>Keep and compare old versions <p> When you have a working version of your code, save it before you add to the code.\
              This will give you something to go back to if you introduce too many new bugs.</p></li>\
           </ol>']]

stage2_lesson5 = [['List Operations: append(), " + " and len()', '<ul>\
              		<li><span class="bold">Append</span> adds a new element to the end of our list. It does not create a new list, it mutates the old list</li>\
                	<li><p><span class="code"><span class="blue">lists</span>.append(<span class="blue">&lt;element&gt;</span>) <br>\
                                  cities = ["Tokyo", "NY", "London"]<br>\
                                  cities.append("Moscow") <br>\
                                  >>> ["Tokyo", "NY", "London", "Moscow"]</span></p></li>\
              		<li> <span class="bold">"+" Generally written in the form: <span class="code"><span class="blue">&lt;list&gt; + &lt;list&gt;</span>\
                          </span></span></li>\
              		<li>This is the like concatenetion, it adds elements of two lists to form a new list <p><span class="code">[1,2,3,4] + [5,6,7,8]<br>\
                    		>>> [1,2,3,4,5,6,7,8] as output</span></p></li>\
              		<li><span class="bold">len() </span></li>\
              		<li>len() is short for length. It checks the length or number of elements in a list or string or any object that has \
              		a collection of things. <p><span class="code">n = [0,1,2,3,4,5,6,7,8,9] <br>len(n) -> 10 </span> </p> </li>\
            	</ul> '],
	    ['The "For Loop"', 'The <span class="bold">For Loop</span>, like other functions is used to execute the body of a function. \
          			<br>The first line starts with: \
           			<span class="bold">for</span>, followed by an element <span class="bold">name</span>, then an <span class="bold">in</span>,\
           			followed by the <span class="bold">test</span> list and end with a colon"<span class="bold">:</span>". The next line starts\
           			with an indentation before the block of codes. <br><br>\
           			<span class="code">for <span class="blue">&lt;name&gt;</span> in <span class="blue">&lt;test&gt;</span>:<br>\
              			&nbsp;&nbsp;<span class="blue">&lt;Block&gt;</span> </span> <br><br>\
          			The <span class="bold">for loop</span>, takes each element "e" <span class="bold">in</span> a <span class="bold">test list</span>, \
          			assign that element to a  <span class="bold">name</span> and evaluate the body, (<span class="bold">block</span> of codes)<br><br>\
          			Let us try this in the following function which take as inputs, a list of numbers and return the sum of all the elements in the input.\
          			<br><br><span class="code">\
          			def sum_list(s): <br>\
                                &nbsp;&nbsp;total = 0 <br>\
                                &nbsp;&nbsp;for e in s: <br>\
                                &nbsp;&nbsp;&nbsp;&nbsp;total = total + e <br>\
                                &nbsp;&nbsp;return total </span> <br><br>\
          			Initial total is "0". We go into the loop, take any element "e" in our list "s", add it to our total to get a new total.\
                                We continue this way till we finish adding all the elements in the list, then return the (grand) total. <br>\
          			When we call this function: <br><br>\
          			<span class="code">print sum_list([1,2,3,4,5]) </span> <br>\
           			We get: <br>\
          			<span class="code">Output: 15 </span>'],
		['Index', '<span class="bold">Index</span> gives the first place where a target element appears in a list. In the case of a multiple occurrence of\
		    the  target, it will keep giving the first occurrence. If the target is not found, it returns an error(it does not return -1)<br><br>\
		    It takes the form:\
          		<span class="code">\
            		<span class="blue">&lt;list&gt;</span>\
            		<span class="bold">.index</span>\
            		<span class="blue">&lt;value&gt;</span></span>  <br>\
            		Example:<br><br>\
          		<span class="code"> p = [0,1,2,3,4,5]<br>\
            		print p.index(3) <br>\
            		>>> 3 <br><br>\
            		p = [0,1,2,3,3,3] <br>\
            		print p.index(3) <br>\
            		>>> 3 (same even for multiple occurrences) <br><br>\
            		print p.index(8) <br>\
            		>>> Error message: 8 is not in the list</span>'],
		 ['The "In" Operation', 'The <span class="bold">in</span> operator allows us to use <span class="bold">index </span>to find elements "in a list".\
		This <span class="bold">in</span> is different from the one we saw in the "for loop" <br>\
          	The syntax is to enable us write a <span class="bold">value</span> to the left of the <span class="bold">in</span> word,\
          	and the <span class="bold">list</span> on the right of "in".<br>\
          	<span class="code"> <span class="blue">&lt;value&gt; </span><span class="bold">in</span>\
          	<span class="blue">&lt;list&gt; </span></span> <br>\
          	Areas where we can perform the <span class="bold">in</span> operations.\
          	<ul>\
          			<li><span class="code"> <span class="blue">&lt;value&gt; </span>\
              			<span class="bold"> in</span>\
              			<span class="blue">&lt;list&gt;</span></span>\
              			  <ul>\
              			    <li>If <span class="blue">&lt;value&gt;</span> is <span class="bold"> in</span> <span class="blue">&lt;list&gt; </span>: True</li>\
              			    <li>Value not in list: False</li>\
                                  </ul></li>\
          			<li><span class="code"> <span class="blue">&lt;value&gt; </span>\
              			<span class="bold"> not in</span> <span class="blue">&lt;list&gt; </span> </span>\
                                    <ul>\
              				<li>The opposite of <span class="blue">&lt;value&gt; </span> <span class="bold"> in</span> <span class="blue">&lt;list&gt;\
              				</span></li>\
              				<li>Value not in list: True</li>\
             				<li>Value in list: False</li>\
				    </ul></li>\
          			<li><span class="code"><span class="blue">&lt;value&gt; </span>\
              			<span class="bold">not in</span> <span class="blue">&lt;list&gt; </span> is equivalent to\
              			<span class="bold"> not</span>(<span class="blue">&lt;value&gt; </span> <span class="bold"> in</span>\
              			<span class="blue">&lt;list&gt; </span>)</span></li>\
        		</ul> <br><br>\
        		Using "index" and "in" to solve a problem <br><br>\
          			<span class="code">def find_element(p,t): <br>\
           			&nbsp;&nbsp;if t in p: <br>\
           			&nbsp;&nbsp; &nbsp;&nbsp;return p.index(t) <br>\
           			&nbsp;&nbsp;else: <br>\
           			&nbsp;&nbsp; &nbsp;&nbsp;return -1 </span>\
           			<br><br>\
           			Solving same problem using "index" and "not in" <br><br>\
          			<span class="code">\
          			def find_target(p,t): <br>\
           			&nbsp;&nbsp;if t not in p: <br>\
           			&nbsp;&nbsp; &nbsp;&nbsp;return -1 <br>\
          		 	&nbsp;&nbsp;else: <br>\
           			&nbsp;&nbsp; &nbsp;&nbsp;return p.index(t) </span><br><br>\
           			When we call these functions, <span class="bold">find_element</span> and <span class="bold">find_target</span> to\
           			find the elements "3" and "5" in the list [1,2,3,4]<br><br>\
          			<span class="code">\
            		find_element([1,2,3,4], 3)<br>\
            		Ouptput: 2<br><br>\
            		find_target([1,2,3,4], 3)<br>\
            		Ouptput: 2<br><br>\
            		find_element([1,2,3,4], 5)<br>\
            		Ouptput: -1<br><br>\
            		find_target([1,2,3,4], 5)<br>\
            		Ouptput: -1 </span><br><br>\
          			All outputs are the same for both functions ("in" and "not in") in all cases.'],
	 ['How to Solve Problems', 'Do not Panic!<br> When you see a complex problem, don ot panic, take a look, think!\
                        And take the following steps to solve programming problems. <br>\
      			    <ol>\
      				<li>What are the inputs? <p>The first step is to understand what the inputs are and how the inputs are presented </p></li>\
      				<li> What are the outputs? <p>The next step is to know the expected outputs are.</p></li>\
      				<li>Solve the problem. <p>Consider how you would solve the problem as a human. Look for simple ways to solve the problem </p></li>\
      				<li>Simple mechanical solution.<p>Write small bits of code, test them to see how they work and what they do.\
                                    Continue to work incrementally till you solve the problem</p></li>\
                            </ol>']]
