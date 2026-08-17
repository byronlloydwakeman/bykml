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

<h2>Automated releases</h2>
<p>This repository uses <strong>Conventional Commits</strong> and <strong>python-semantic-release</strong> for automated versioning and changelog generation.</p>
<ul>
    <li><code>fix:</code> commits trigger a patch release</li>
    <li><code>feat:</code> commits trigger a minor release</li>
    <li><code>feat!:</code> or <code>BREAKING CHANGE:</code> trigger a major release</li>
</ul>
<p>On pushes to <code>main</code>, GitHub Actions runs CI, computes the next semantic version, updates <code>CHANGELOG.md</code>, tags the release, builds distributions, and publishes to PyPI using trusted publishing (OIDC).</p>
<p>For release history, see <a href="./CHANGELOG.md">CHANGELOG.md</a>.</p>