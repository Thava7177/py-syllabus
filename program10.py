import webbrowser
f=open("helloweb.html","w")
bro='''<html>
<head>
<script>
function calculate()
{
name=document.getElementById("name").value;
pamount=document.getElementById("pamount").value;
inamount=document.getElementById("inamount").value;
noofyear=document.getElementById("noofyear").value;
RESULT=document.getElementById("RESULT");
RESULT.innerHTML="THE INSTREAST IS "+((pamount*inamount*noofyear)/100)
}
</script>
</head>
<body>
<h1>SIMPLE INTREAST CALCULATION</h><br/>
Name :<input id="name"><br/>
Principle Amount :<input id="pamount"><br/>
Rate Of Intreast :<input id="inamount"><br/>
NO.OF.Year :<input id="noofyear"><br/>
<button onclick="calculate()">Calculate<br/>
<p id="RESULT"></p>
</body>
</html>'''
f.write(bro)
f.close()
webbrowser.open_new_tab('helloweb.html')
