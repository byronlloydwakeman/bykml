<h2>Introduction</h2>

<p>bykml is a library to easily read, write and update KML files. 
It's built around using dictionaries to easily replace values and add kml elements.</p>

<h2>Documentation</h2>
<p>kmlfactory file inside the bykml package has a KmlFactory class and a placemark_template function 
used to create placemarks and add to the 
</p>

<h2>Install</h2>
<p>You can install the package with ```pip install bykml```</p>

<h2>Dependencies</h2>
<ul>
    <li><a href="https://pypi.org/project/xmltodict/">xmltodict</a></li>
</ul>

<h2>Limitations</h2>
<p>Due to the nature of dictionaries of only being able to have one key per value.
This subsequently means that lists have to be used to have multiple items within the same kml tag.
For example if we have a 'Folder' tag which will contain a number of placemarks, 
we cannot have a nested folder with multiple placemarks inside.
This is currently being reviewed for a solution.</p>

<h2>Changelog</h2>
<h3>1.5.0 (29/04/2024)</h3>
<ul>
    <li>Updated placemark template to accept images</li>
    <li>Updated function comments</li>
</ul>

<h3>1.4.0 (22/01/2024)</h3>
<ul>
    <li>Added kmlfactory</li>
</ul>

<h3>1.3.0 (22/01/2024)</h3>
<ul>
    <li>Updated README</li>
</ul>

<h3>1.2.0 (22/01/2024)</h3>
<ul>
    <li>Updated maintainers</li>
</ul>

<h3>1.1.0 (21/01/2024)</h3>
<ul>
    <li>Initial release</li>
</ul>