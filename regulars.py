import re
import pprint

#if not respond.ok:
#    raise AssertionError("Page not found!!!")

text = """<p><strong>Beginner</strong></p>
<ul>
<li><a href="https://pythonspot.com/en/introduction/">Introduction</a></li>
<li><a href="https://pythonspot.com/en/python-strings/">Text input and output </a></li>
<li><a href="https://pythonspot.com/en/string-slices-part-2/">String slices</a></li>
<li><a href="https://pythonspot.com/en/python-variables/">Variables</a></li>
<li><a href="https://pythonspot.com/en/python-lists/">Lists</a></li>
<li><a href="https://pythonspot.com/en/if-statements/">If statements</a></li>
<li><a href="https://pythonspot.com/en/functions/">Functions</a></li>
<li><a href="https://pythonspot.com/en/global-local-variables/">Global and Local variables</a></li>
<li><a href="https://pythonspot.com/en/scope">Scope</a></li>
<li><a href="https://pythonspot.com/en/loops/">Loops</a></li>
<li><a href="https://pythonspot.com/en/python-tuples/">Tuples</a></li>
<li><a href="https://pythonspot.com/en/python-dictionaries/">Dictionaries</a></li>
<li><a href="https://pythonspot.com/en/datatype-casting/">Datatype casting</a></li>
<li><a href="https://pythonspot.com/en/random-numbers/">Random numbers</a></li>
<li><a href="https://pythonspot.com/en/read-file/">Read file</a></li>
<li><a href="https://pythonspot.com/en/write-file/">Write file</a></li>
<li><a href="https://pythonspot.com/en/objects-and-classes">Objects and classes</a></li>
<li><a href="https://pythonspot.com/en/encapsulation">Encapsulation</a></li>
<li><a href="https://pythonspot.com/en/method-overloading/">Method overloading</a></li>
<li><a href="https://pythonspot.com/en/inheritance/">Inheritance</a></li>
<li><a href="https://pythonspot.com/en/poylmorphism/">Polymorphism</a></li>
<li><a href="https://pythonspot.com/en/inner-classes">Inner classes</a></li>
<li><a href="https://pythonspot.com/en/factory-method/">Factory method</a></li>
<li><a href="https://pythonspot.com/en/recursion/">Recursive functions</a></li>
<li><a href="https://pythonspot.com/en/logging/">Logging</a></li>
<li><a href="https://pythonspot.com/en/python-subprocess/">Subprocess</a></li>
<li><a href="https://pythonspot.com/en/threading">Threading</a></li>
<li><a href="https://pythonspot.com/en/python-lambda/">Lambda</a></li>
<li><a href="https://pythonspot.com/en/python-set/">Sets</a></li>
<li><a href="https://pythonspot.com/en/python-modules/">Modules</a></li>
<li><a href="https://pythonspot.com/en/python-graph/">Graphs</a></li>
<li><a href="https://pythonspot.com/en/python-finite-state-machine/">State Machine</a></li>
<li><a href="https://pythonspot.com/en/python-tree">Tree</a></li>
<li><a href="https://pythonspot.com/en/binary-numbers-and-logical-operators/">Binary numbers</a></li>
<li><a href="https://pythonspot.com/en/python-debugging/">Python Debugging</a></li>
</ul>"""
#-------- method with compiling of template --------
"""
template = re.compile('<li><a href="(.*?)">(.*?)<')

result = template.findall(text, re.IGNORECASE | re.MULTILINE)
result = template.search(text, re.I | re.M) # this method has .groups

pprint.pprint(result.groups())
"""

#-------- method without compiling of template --------

for line in text.split("\n"):
    result = re.search('<li><a href="(.*?)">(.*?)<', line)
    if result:
        print(result.groups())
