import pandas as pd
from bs4 import BeautifulSoup

html_string ='''
<table id="resultTable" cellpadding="1" cellspacing="1" width="1070">
<thead> <tr>
<th width="80">Brand</th>
<th width="100">Model</th>
<th width="200">Spec</th>
<th width="60">Year</th>
<th width="90">dB at idle</th>
<th width="90">dB at 50km/h</th>
<th width="90">dB at 80km/h</th>
<th width="90">dB at 100km/h</th>
<th width="90">dB at 120km/h</th>
<th width="90">dB at 140km/h</th>
<th width="90"><a href="index.html">mph</a></th>
</tr>
</thead> <tbody>
<tr>
</tr>
<tr>
<td>Abarth</td><td>500</td><td>1.4 16v T-Jet</td><td>2008</td><td> 47.3 </td><td> 58.2 </td><td> 67.0 </td><td> 70.2 </td><td> 72.9 </td><td> 76.0 </td></tr>
<tr><td>Abarth</td><td>595</td><td>Competizione</td><td>2017</td><td> 49.9 </td><td> 65.7 </td><td> 69.0 </td><td> 72.3 </td><td> 73.1 </td><td> 75.8 </td></tr>
<tr><td>Acura</td><td>MDX</td><td>3.5 V6</td><td>2013</td><td> 41.7 </td><td> 51.7 </td><td> 57.9 </td><td> 61.2 </td><td> 64.0 </td><td> 66.8 </td></tr>
<tr><td>Acura</td><td>RDX</td><td>3.5 V6</td><td>2012</td><td> 43.0 </td><td> 54.4 </td><td> 61.5 </td><td> 65.5 </td><td> 67.7 </td><td> 69.9 </td></tr>
<tr><td>Acura</td><td>RL</td><td>3.7 V6</td><td>2009</td><td> 43.6 </td><td> 55.5 </td><td> 63.0 </td><td> 66.9 </td><td> 70.2 </td><td> 73.5 </td></tr>
<tr><td>Acura</td><td>RLX</td><td>3.5 V6</td><td>2013</td><td> 39.5 </td><td> 49.7 </td><td> 56.0 </td><td> 59.3 </td><td> 62.4 </td><td> 65.6 </td></tr>
<tr><td>Acura</td><td>RLX</td><td>3.5 V6</td><td>2016</td><td> 42.2 </td><td> 51.1 </td><td> 56.7 </td><td> 59.4 </td><td> 62.6 </td><td> 65.9 </td></tr>
<tr><td>Acura</td><td>TL</td><td>3.5 V6</td><td>2009</td><td> 40.2 </td><td> 54.5 </td><td> 63.3 </td><td> 68.6 </td><td> 70.1 </td><td> 71.7 </td></tr>
<tr><td>Acura</td><td>TL</td><td>3.7 V6</td><td>2010</td><td> 39.9 </td><td> 48.4 </td><td> 53.8 </td><td> 56.2 </td><td> 60.2 </td><td> 64.2 </td></tr>
<tr><td>Acura</td><td>TSX</td><td>2.4</td><td>2009</td><td> 42.2 </td><td> 54.0 </td><td> 61.2 </td><td> 65.2 </td><td> 67.9 </td><td> 70.5 </td></tr>
<tr><td>Acura</td><td>TSX</td><td>V6</td><td>2010</td><td> 42.4 </td><td> 54.3 </td><td> 61.7 </td><td> 65.5 </td><td> 69.0 </td><td> 72.6 </td></tr>
<tr><td>Acura</td><td>TSX</td><td>Stationcar</td><td>2011</td><td> 48.8 </td><td> 56.7 </td><td> 61.7 </td><td> 64.2 </td><td> 66.6 </td><td> 69.1 </td></tr>
<tr><td>Alfa Romeo</td><td>147</td><td>1.9 JTDm</td><td>2008</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 67.0 </td><td> 69.1 </td><td> 71.4 </td></tr>
<tr><td>Alfa Romeo</td><td>159</td><td>2.2 JTS</td><td>2008</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 67.2 </td><td> 68.5 </td><td> 70.2 </td></tr>
<tr><td>Alfa Romeo</td><td>159</td><td>2.2 JTS Selespeed</td><td>2008</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 67.2 </td><td> 68.5 </td><td> 70.2 </td></tr>
<tr><td>Alfa Romeo</td><td>4C</td><td>&nbsp;</td><td>2014</td><td> 50.1 </td><td> 75.2 </td><td> 76.1 </td><td> 76.9 </td><td> 81.3 </td><td> 83.3 </td></tr>
<tr><td>Alfa Romeo</td><td>Giulia</td><td>2.1d</td><td>2017</td><td> 44.9 </td><td> 59.8 </td><td> 63.5 </td><td> 67.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Alfa Romeo</td><td>Giulia</td><td>2.9 V6</td><td>2017</td><td> 47.9 </td><td> 60.8 </td><td> 64.0 </td><td> 67.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Alfa Romeo</td><td>Giulietta</td><td>1.4</td><td>2010</td><td> 44.1 </td><td> 60.5 </td><td> 64.0 </td><td> 66.0 </td><td> 68.5 </td><td> 71.5 </td></tr>
<tr><td>Alfa Romeo</td><td>Giulietta</td><td>1.6 JTDm</td><td>2011</td><td> 43.7 </td><td> 53.8 </td><td> 61.9 </td><td> 66.2 </td><td> 67.3 </td><td> 68.8 </td></tr>
<tr><td>Alfa Romeo</td><td>Giulietta</td><td>1.4T</td><td>2012</td><td> 42.1 </td><td> 58.8 </td><td> 61.1 </td><td> 63.5 </td><td> 66.5 </td><td> 68.3 </td></tr>
<tr><td>Alfa Romeo</td><td>Giulietta</td><td>2.0 JTDm</td><td>2012</td><td> 45.2 </td><td> 55.7 </td><td> 64.0 </td><td> 68.0 </td><td> 69.6 </td><td> 71.6 </td></tr>
<tr><td>Alfa Romeo</td><td>GT</td><td>1.9 JTDm Q2</td><td>2008</td><td> 41.9 </td><td> 51.5 </td><td> 59.2 </td><td> 63.8 </td><td> 64.4 </td><td> 65.3 </td></tr>
<tr><td>Alfa Romeo</td><td>MiTo</td><td>1.4 Turbo 155</td><td>2008</td><td> 45.1 </td><td> 55.5 </td><td> 63.8 </td><td> 68.5 </td><td> 69.4 </td><td> 70.7 </td></tr>
<tr><td>Alfa Romeo</td><td>MiTo</td><td>1.6 JTDm</td><td>2009</td><td> 46.6 </td><td> 57.4 </td><td> 66.0 </td><td> 70.3 </td><td> 71.7 </td><td> 73.5 </td></tr>
<tr><td>Alfa Romeo</td><td>MiTo</td><td>1.4 Turbo Multi-Air</td><td>2010</td><td> 42.0 </td><td> 62.3 </td><td> 66.4 </td><td> 68.5 </td><td> 72.9 </td><td> 75.7 </td></tr>
<tr><td>Alfa Romeo</td><td>Stelvio</td><td>2.0</td><td>2017</td><td> 42.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Alfa Romeo</td><td>Stelvio</td><td>2.1d</td><td>2017</td><td> 43.9 </td><td> 53.8 </td><td> 58.3 </td><td> 61.7 </td><td> 67.6 </td><td> 67.7 </td></tr>
<tr><td>Alpina</td><td>B7</td><td>&nbsp;</td><td>2011</td><td> 43.9 </td><td> 54.8 </td><td> 61.5 </td><td> 65.5 </td><td> 67.1 </td><td> 68.8 </td></tr>
<tr><td>Aston Martin</td><td>Rapide</td><td>5.9 V12</td><td>2013</td><td> 52.2 </td><td> 58.1 </td><td> 62.2 </td><td> 63.1 </td><td> 68.6 </td><td> 74.1 </td></tr>
<tr><td>Audi</td><td>A1</td><td>1.4 TFSI S tronic</td><td>2010</td><td> 39.4 </td><td> 62.2 </td><td> 64.4 </td><td> 66.8 </td><td> 69.1 </td><td> 71.9 </td></tr>
<tr><td>Audi</td><td>A1</td><td>1.4</td><td>2014</td><td> 38.2 </td><td> 59.1 </td><td> 63.3 </td><td> 66.1 </td><td> 69.1 </td><td> 71.3 </td></tr>
<tr><td>Audi</td><td>A3</td><td>2.0 TFSI Cabrio</td><td>2008</td><td> 46.1 </td><td> 62.0 </td><td> 63.0 </td><td> 65.0 </td><td> 68.0 </td><td> 68.2 </td></tr>
<tr><td>Audi</td><td>A3</td><td>1.4 TFSI S-Tronic</td><td>2009</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 68.6 </td><td> 69.2 </td><td> 70.2 </td></tr>
<tr><td>Audi</td><td>A3</td><td>1.2 TSI Cabrio</td><td>2010</td><td> 39.9 </td><td> 60.3 </td><td> 65.5 </td><td> 67.8 </td><td> 70.9 </td><td> 72.9 </td></tr>
<tr><td>Audi</td><td>A3</td><td>1.4 TFSI Stationcar</td><td>2010</td><td> 36.6 </td><td> 61.5 </td><td> 65.0 </td><td> 66.5 </td><td> 68.0 </td><td> 69.9 </td></tr>
<tr><td>Audi</td><td>A3</td><td>1.2 TFSI Stationcar</td><td>2011</td><td> 37.1 </td><td> 58.5 </td><td> 64.0 </td><td> 65.4 </td><td> 68.3 </td><td> 71.6 </td></tr>
<tr><td>Audi</td><td>A3</td><td>1.4 TFSI</td><td>2012</td><td> 38.2 </td><td> 57.6 </td><td> 61.4 </td><td> 62.5 </td><td> 65.1 </td><td> 68.1 </td></tr>
<tr><td>Audi</td><td>A3</td><td>1.8 TFSI</td><td>2012</td><td> 44.5 </td><td> 58.0 </td><td> 62.7 </td><td> 65.9 </td><td> 68.7 </td><td> 70.7 </td></tr>
<tr><td>Audi</td><td>A3</td><td>1.8 Stationcar</td><td>2013</td><td> 47.2 </td><td> 58.2 </td><td> 61.2 </td><td> 65.2 </td><td> 67.9 </td><td> 70.6 </td></tr>
<tr><td>Audi</td><td>A3</td><td>2.0 TDI</td><td>2013</td><td> 43.0 </td><td> 53.0 </td><td> 60.9 </td><td> 63.5 </td><td> 66.3 </td><td> 69.5 </td></tr>
<tr><td>Audi</td><td>A3</td><td>1.8 TFSI Cabrio</td><td>2014</td><td> 39.2 </td><td> 55.6 </td><td> 60.2 </td><td> 64.4 </td><td> 67.4 </td><td> 71.3 </td></tr>
<tr><td>Audi</td><td>A3</td><td>2.0</td><td>2014</td><td> 40.4 </td><td> 51.7 </td><td> 58.6 </td><td> 62.5 </td><td> 64.9 </td><td> 67.2 </td></tr>
<tr><td>Audi</td><td>A3</td><td>G-Tron</td><td>2014</td><td> 42.5 </td><td> 54.0 </td><td> 59.5 </td><td> 62.9 </td><td> 65.5 </td><td> 70.4 </td></tr>
<tr><td>Audi</td><td>A3</td><td>1.0</td><td>2016</td><td> 39.9 </td><td> 56.8 </td><td> 59.5 </td><td> 62.2 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Audi</td><td>A3</td><td>1.4 Cabrio</td><td>2016</td><td> 40.0 </td><td> 57.6 </td><td> 62.1 </td><td> 65.7 </td><td> 69.9 </td><td> 72.6 </td></tr>
<tr><td>Audi</td><td>A3</td><td>2.0 TDI Stationcar</td><td>2016</td><td> 42.9 </td><td> 59.8 </td><td> 62.0 </td><td> 64.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Audi</td><td>A4</td><td>1.8 TFSI</td><td>2008</td><td> 41.6 </td><td> 57.8 </td><td> 61.5 </td><td> 64.3 </td><td> 66.4 </td><td> 69.7 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TDI</td><td>2008</td><td> 43.2 </td><td> 53.1 </td><td> 61.1 </td><td> 65.2 </td><td> 66.4 </td><td> 68.0 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TDI Stationcar</td><td>2008</td><td> 44.3 </td><td> 54.5 </td><td> 62.7 </td><td> 64.8 </td><td> 68.2 </td><td> 72.0 </td></tr>
<tr><td>Audi</td><td>A4</td><td>3.2 V6</td><td>2009</td><td> 43.9 </td><td> 53.8 </td><td> 59.9 </td><td> 63.1 </td><td> 65.8 </td><td> 68.4 </td></tr>
<tr><td>Audi</td><td>A4</td><td>1.8 TFSI</td><td>2011</td><td> 45.5 </td><td> 56.0 </td><td> 64.4 </td><td> 67.4 </td><td> 70.1 </td><td> 73.2 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TFSI Allroad</td><td>2011</td><td> 42.8 </td><td> 52.6 </td><td> 60.5 </td><td> 64.4 </td><td> 65.8 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TDI</td><td>2012</td><td> 43.6 </td><td> 53.6 </td><td> 61.6 </td><td> 63.7 </td><td> 67.1 </td><td> 70.9 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TDIe</td><td>2012</td><td> 42.9 </td><td> 57.2 </td><td> 60.9 </td><td> 63.3 </td><td> 66.0 </td><td> 69.3 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TFSI</td><td>2012</td><td> 44.4 </td><td> 54.0 </td><td> 59.9 </td><td> 63.2 </td><td> 65.2 </td><td> 67.2 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 T</td><td>2014</td><td> 43.2 </td><td> 53.2 </td><td> 59.4 </td><td> 62.9 </td><td> 64.7 </td><td> 66.4 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TDI Stationcar</td><td>2014</td><td> 41.0 </td><td> 55.2 </td><td> 59.1 </td><td> 62.9 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>Audi</td><td>A4</td><td>3.0 TDI Stationcar</td><td>2014</td><td> 41.6 </td><td> 55.2 </td><td> 59.6 </td><td> 63.9 </td><td> 66.3 </td><td> 68.1 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TDI</td><td>2015</td><td> 45.2 </td><td> 54.3 </td><td> 58.6 </td><td> 61.6 </td><td> 64.9 </td><td> 68.6 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TDI Stationcar</td><td>2015</td><td> 43.8 </td><td> 55.5 </td><td> 60.9 </td><td> 63.7 </td><td> 67.4 </td><td> 70.6 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TDI</td><td>2016</td><td> 40.9 </td><td> 56.8 </td><td> 59.0 </td><td> 61.2 </td><td> 64.1 </td><td> 67.4 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TFSI</td><td>2016</td><td> 42.9 </td><td> 54.8 </td><td> 58.0 </td><td> 61.2 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>A4</td><td>2.0 TDI</td><td>2017</td><td> 44.9 </td><td> 56.8 </td><td> 59.5 </td><td> 62.2 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>A5</td><td>3.0 TDI Quattro</td><td>2008</td><td> 44.1 </td><td> 54.3 </td><td> 62.5 </td><td> 67.6 </td><td> 67.9 </td><td> 68.5 </td></tr>
<tr><td>Audi</td><td>A5</td><td>3.2 FSI Quattro Tiptronic</td><td>2009</td><td> 42.8 </td><td> 52.6 </td><td> 60.5 </td><td> 64.0 </td><td> 65.8 </td><td> 68.0 </td></tr>
<tr><td>Audi</td><td>A5</td><td>2.0 TFSI Cabrio</td><td>2010</td><td> 39.6 </td><td> 61.5 </td><td> 63.2 </td><td> 66.6 </td><td> 69.2 </td><td> 71.8 </td></tr>
<tr><td>Audi</td><td>A5</td><td>3.2 FSI Quattro</td><td>2010</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 66.4 </td><td> 68.0 </td><td> 70.0 </td></tr>
<tr><td>Audi</td><td>A5</td><td>1.8 TFSI Sportback</td><td>2012</td><td> 44.1 </td><td> 54.2 </td><td> 62.4 </td><td> 65.1 </td><td> 67.9 </td><td> 71.1 </td></tr>
<tr><td>Audi</td><td>A5</td><td>2.0 TFSI</td><td>2016</td><td> 37.9 </td><td> 55.8 </td><td> 59.5 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Audi</td><td>A6</td><td>2.0 TDIe</td><td>2009</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 64.4 </td><td> 67.2 </td><td> 70.4 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TFSI Quattro</td><td>2009</td><td> 43.6 </td><td> 53.6 </td><td> 61.6 </td><td> 66.3 </td><td> 67.0 </td><td> 68.0 </td></tr>
<tr><td>Audi</td><td>A6</td><td>2.8 FSI Tiptronic Quattro Stationcar</td><td>2010</td><td> 43.4 </td><td> 57.8 </td><td> 62.1 </td><td> 64.8 </td><td> 66.7 </td><td> 69.2 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TDI</td><td>2010</td><td> 45.6 </td><td> 58.0 </td><td> 61.8 </td><td> 65.0 </td><td> 67.7 </td><td> 70.8 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TDI Quattro</td><td>2011</td><td> 42.2 </td><td> 57.5 </td><td> 61.6 </td><td> 62.4 </td><td> 65.4 </td><td> 67.5 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TFSI</td><td>2011</td><td> 42.8 </td><td> 52.7 </td><td> 60.6 </td><td> 64.1 </td><td> 65.9 </td><td> 68.1 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TFSI Stationcar</td><td>2011</td><td> 38.7 </td><td> 52.7 </td><td> 58.3 </td><td> 61.3 </td><td> 64.5 </td><td> 66.6 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TDI Stationcar</td><td>2012</td><td> 44.0 </td><td> 54.2 </td><td> 62.3 </td><td> 65.2 </td><td> 67.8 </td><td> 70.8 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TFSI Quattro</td><td>2012</td><td> 42.0 </td><td> 52.5 </td><td> 59.0 </td><td> 62.7 </td><td> 64.9 </td><td> 67.2 </td></tr>
<tr><td>Audi</td><td>A6</td><td>2.0 TDI</td><td>2015</td><td> 45.1 </td><td> 57.5 </td><td> 61.5 </td><td> 64.0 </td><td> 66.0 </td><td> 67.5 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TDI</td><td>2015</td><td> 41.6 </td><td> 56.2 </td><td> 60.1 </td><td> 63.9 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>Audi</td><td>A6</td><td>2.0 TDI</td><td>2016</td><td> 43.9 </td><td> 53.1 </td><td> 57.3 </td><td> 60.1 </td><td> 64.0 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>A6</td><td>2.0 TDI</td><td>2016</td><td> 39.9 </td><td> 59.8 </td><td> 61.5 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>A6</td><td>2.0 TDI Stationcar</td><td>2016</td><td> 41.9 </td><td> 57.8 </td><td> 60.5 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TDI</td><td>2016</td><td> 48.1 </td><td> 57.2 </td><td> 61.2 </td><td> 65.3 </td><td> 66.3 </td><td> 69.7 </td></tr>
<tr><td>Audi</td><td>A6</td><td>2.0 TDI</td><td>2017</td><td> 40.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>A6</td><td>2.0 TFSI</td><td>2017</td><td> 39.9 </td><td> 53.8 </td><td> 58.5 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TDI</td><td>2017</td><td> 41.9 </td><td> 56.8 </td><td> 60.5 </td><td> 64.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Audi</td><td>A6</td><td>3.0 TDI stationcar</td><td>2017</td><td> 39.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Audi</td><td>A7</td><td>3.0 TFSI</td><td>2011</td><td> 42.9 </td><td> 52.8 </td><td> 60.7 </td><td> 65.1 </td><td> 66.0 </td><td> 67.2 </td></tr>
<tr><td>Audi</td><td>A8</td><td>2.8 FSIe</td><td>2008</td><td> 42.7 </td><td> 52.6 </td><td> 60.4 </td><td> 63.5 </td><td> 65.8 </td><td> 68.3 </td></tr>
<tr><td>Audi</td><td>A8</td><td>4.2 TDI Quattro</td><td>2010</td><td> 41.7 </td><td> 51.3 </td><td> 59.0 </td><td> 63.3 </td><td> 64.1 </td><td> 65.2 </td></tr>
<tr><td>Audi</td><td>A8</td><td>4.2 V8 FSI</td><td>2010</td><td> 36.6 </td><td> 54.6 </td><td> 58.6 </td><td> 60.7 </td><td> 62.4 </td><td> 65.4 </td></tr>
<tr><td>Audi</td><td>A8</td><td>4.2 V8</td><td>2011</td><td> 45.8 </td><td> 54.1 </td><td> 59.3 </td><td> 62.0 </td><td> 64.0 </td><td> 66.1 </td></tr>
<tr><td>Audi</td><td>A8</td><td>4.0 V8</td><td>2012</td><td> 40.4 </td><td> 51.0 </td><td> 57.5 </td><td> 61.1 </td><td> 63.1 </td><td> 65.1 </td></tr>
<tr><td>Audi</td><td>A8</td><td>3.0 TDI</td><td>2014</td><td> 39.7 </td><td> 54.2 </td><td> 57.6 </td><td> 60.9 </td><td> 64.7 </td><td> 66.3 </td></tr>
<tr><td>Audi</td><td>Q2</td><td>1.4</td><td>2017</td><td> 37.9 </td><td> 60.8 </td><td> 63.0 </td><td> 65.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Audi</td><td>Q3</td><td>2.0 TDI Quattro</td><td>2011</td><td> 43.9 </td><td> 57.0 </td><td> 61.6 </td><td> 64.6 </td><td> 67.6 </td><td> 71.8 </td></tr>
<tr><td>Audi</td><td>Q3</td><td>2.0</td><td>2015</td><td> 42.3 </td><td> 57.2 </td><td> 61.1 </td><td> 64.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Audi</td><td>Q3</td><td>2.0</td><td>2016</td><td> 41.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Audi</td><td>Q3</td><td>2.0 TDI</td><td>2016</td><td> 47.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Audi</td><td>Q3 RS</td><td>&nbsp;</td><td>2015</td><td> 42.9 </td><td> 58.2 </td><td> 62.1 </td><td> 65.9 </td><td> 68.6 </td><td> 70.3 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>3.0 TDI</td><td>2008</td><td> 44.8 </td><td> 57.3 </td><td> 61.1 </td><td> 63.8 </td><td> 67.3 </td><td> 69.6 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>2.0 TDI Quattro</td><td>2009</td><td> 43.1 </td><td> 53.0 </td><td> 61.0 </td><td> 64.8 </td><td> 66.3 </td><td> 68.2 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>3.2 V6</td><td>2009</td><td> 45.3 </td><td> 54.5 </td><td> 60.2 </td><td> 63.2 </td><td> 65.6 </td><td> 68.0 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>2.0 TDI Quattro</td><td>2011</td><td> 45.4 </td><td> 59.0 </td><td> 63.0 </td><td> 66.8 </td><td> 67.5 </td><td> 71.5 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>2.0</td><td>2012</td><td> 42.8 </td><td> 52.7 </td><td> 60.6 </td><td> 64.2 </td><td> 65.9 </td><td> 68.0 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>3.0 V6</td><td>2012</td><td> 47.8 </td><td> 55.8 </td><td> 60.8 </td><td> 63.6 </td><td> 65.2 </td><td> 66.8 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>2.0</td><td>2014</td><td> 38.2 </td><td> 53.8 </td><td> 57.8 </td><td> 59.8 </td><td> 63.7 </td><td> 66.2 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>2.0 TDI</td><td>2014</td><td> 41.6 </td><td> 57.2 </td><td> 60.6 </td><td> 63.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>3.0 TDI</td><td>2014</td><td> 41.6 </td><td> 58.2 </td><td> 61.1 </td><td> 63.8 </td><td> 67.3 </td><td> 69.1 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>2.0 TDI</td><td>2016</td><td> 43.9 </td><td> 58.8 </td><td> 61.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>2.0 TDI</td><td>2017</td><td> 41.9 </td><td> 59.8 </td><td> 61.5 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>2.0 TDI</td><td>2017</td><td> 41.9 </td><td> 59.8 </td><td> 61.5 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>Q5</td><td>2.0 TFSI</td><td>2017</td><td> 38.9 </td><td> 54.8 </td><td> 58.5 </td><td> 62.2 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>Q7</td><td>3.0 TDI</td><td>2010</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 66.7 </td><td> 68.8 </td><td> 71.1 </td></tr>
<tr><td>Audi</td><td>Q7</td><td>3.0 TDI</td><td>2015</td><td> 41.2 </td><td> 51.7 </td><td> 56.7 </td><td> 60.2 </td><td> 63.5 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>Q7</td><td>3.0 TDI Hybrid</td><td>2016</td><td> 42.0 </td><td> 50.5 </td><td> 55.8 </td><td> 59.3 </td><td> 63.6 </td><td> 65.7 </td></tr>
<tr><td>Audi</td><td>Q7</td><td>SQ7</td><td>2017</td><td> 42.9 </td><td> 54.8 </td><td> 58.0 </td><td> 61.2 </td><td> 63.3 </td><td> 66.5 </td></tr>
<tr><td>Audi</td><td>R8</td><td>5.2 FSI Quattro R-Tronic</td><td>2009</td><td> 47.8 </td><td> 58.8 </td><td> 67.6 </td><td> 71.3 </td><td> 73.6 </td><td> 76.1 </td></tr>
<tr><td>Audi</td><td>R8</td><td>5.2 FSI</td><td>2010</td><td> 50.6 </td><td> 59.4 </td><td> 65.0 </td><td> 67.3 </td><td> 71.8 </td><td> 76.3 </td></tr>
<tr><td>Audi</td><td>R8</td><td>V10 Plus</td><td>2016</td><td> 49.9 </td><td> 64.7 </td><td> 67.5 </td><td> 69.8 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Audi</td><td>R8</td><td>5.2 V10</td><td>2017</td><td> 50.8 </td><td> 65.7 </td><td> 68.0 </td><td> 70.3 </td><td> 72.1 </td><td> 75.8 </td></tr>
<tr><td>Audi</td><td>R8</td><td>V10 Plus</td><td>2017</td><td> 49.9 </td><td> 65.7 </td><td> 68.0 </td><td> 70.3 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>Audi</td><td>RS4</td><td>Cabrio</td><td>2008</td><td> 47.9 </td><td> 56.9 </td><td> 62.6 </td><td> 65.1 </td><td> 69.2 </td><td> 73.3 </td></tr>
<tr><td>Audi</td><td>RS5</td><td>&nbsp;</td><td>2012</td><td> 44.7 </td><td> 53.3 </td><td> 58.9 </td><td> 61.0 </td><td> 65.7 </td><td> 70.4 </td></tr>
<tr><td>Audi</td><td>RS5</td><td>&nbsp;</td><td>2017</td><td> 44.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Audi</td><td>RS7</td><td>&nbsp;</td><td>2017</td><td> 40.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>S3</td><td>&nbsp;</td><td>2014</td><td> 43.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Audi</td><td>S3</td><td>&nbsp;</td><td>2017</td><td> 47.9 </td><td> 62.7 </td><td> 64.5 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Audi</td><td>S4</td><td>3.0 TFSI Quattro</td><td>2009</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 67.8 </td><td> 68.5 </td><td> 69.6 </td></tr>
<tr><td>Audi</td><td>S5</td><td>&nbsp;</td><td>2008</td><td> 42.9 </td><td> 55.7 </td><td> 63.5 </td><td> 68.0 </td><td> 70.5 </td><td> 73.0 </td></tr>
<tr><td>Audi</td><td>S8</td><td>&nbsp;</td><td>2016</td><td> 39.9 </td><td> 55.8 </td><td> 59.5 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Audi</td><td>SQ5</td><td>3.0 V6</td><td>2014</td><td> 42.7 </td><td> 55.6 </td><td> 58.4 </td><td> 63.3 </td><td> 65.3 </td><td> 68.6 </td></tr>
<tr><td>Audi</td><td>SQ5</td><td>3.0 V6</td><td>2016</td><td> 48.9 </td><td> 58.8 </td><td> 61.5 </td><td> 64.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Audi</td><td>SQ5</td><td>&nbsp;</td><td>2017</td><td> 39.9 </td><td> 58.8 </td><td> 61.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Audi</td><td>SQ7</td><td>&nbsp;</td><td>2017</td><td> 42.9 </td><td> 54.8 </td><td> 58.0 </td><td> 61.2 </td><td> 63.3 </td><td> 66.5 </td></tr>
<tr><td>Audi</td><td>TT</td><td>2.0 TFSI</td><td>2008</td><td> 45.6 </td><td> 56.1 </td><td> 64.5 </td><td> 69.0 </td><td> 70.1 </td><td> 71.6 </td></tr>
<tr><td>Audi</td><td>TT</td><td>3.2</td><td>2008</td><td> 45.3 </td><td> 58.5 </td><td> 66.7 </td><td> 71.3 </td><td> 73.7 </td><td> 76.2 </td></tr>
<tr><td>Audi</td><td>TT</td><td>RS 2.5 TFSI Quattro</td><td>2009</td><td> 48.2 </td><td> 59.3 </td><td> 68.2 </td><td> 73.5 </td><td> 74.1 </td><td> 75.1 </td></tr>
<tr><td>Audi</td><td>TT</td><td>2.0D</td><td>2014</td><td> 43.6 </td><td> 61.2 </td><td> 64.1 </td><td> 66.9 </td><td> 69.6 </td><td> 71.3 </td></tr>
<tr><td>Audi</td><td>TT</td><td>1.8 Cabrio</td><td>2016</td><td> 43.9 </td><td> 59.8 </td><td> 63.5 </td><td> 67.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Audi</td><td>TT</td><td>RS</td><td>2017</td><td> 46.9 </td><td> 61.8 </td><td> 65.5 </td><td> 69.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Audi</td><td>TT</td><td>RS Roadster</td><td>2017</td><td> 50.8 </td><td> 62.7 </td><td> 66.5 </td><td> 70.3 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>Audi</td><td>TT Roadster</td><td>2.0D</td><td>2015</td><td> 44.2 </td><td> 60.2 </td><td> 64.1 </td><td> 67.9 </td><td> 70.6 </td><td> 72.3 </td></tr>
<tr><td>Audi</td><td>TTS</td><td>2.0 TFSI</td><td>2008</td><td> 44.1 </td><td> 54.2 </td><td> 62.4 </td><td> 66.4 </td><td> 67.8 </td><td> 69.6 </td></tr>
<tr><td>Audi</td><td>TTS</td><td>&nbsp;</td><td>2016</td><td> 43.9 </td><td> 62.7 </td><td> 65.0 </td><td> 67.3 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>Audi</td><td>TTS</td><td>Cabrio</td><td>2016</td><td> 47.9 </td><td> 61.8 </td><td> 65.0 </td><td> 68.3 </td><td> 72.1 </td><td> 75.8 </td></tr>
<tr><td>Bentley</td><td>Bentayga</td><td>6.0 W12</td><td>2016</td><td> 37.9 </td><td> 52.8 </td><td> 57.5 </td><td> 62.2 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Bentley</td><td>Bentayga</td><td>4.0d</td><td>2017</td><td> 42.9 </td><td> 53.8 </td><td> 57.0 </td><td> 60.2 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Bentley</td><td>Continental</td><td>Supersports</td><td>2010</td><td> 47.3 </td><td> 57.0 </td><td> 63.0 </td><td> 66.1 </td><td> 69.0 </td><td> 71.9 </td></tr>
<tr><td>Bentley</td><td>Continental GT</td><td>V8</td><td>2012</td><td> 47.6 </td><td> 54.3 </td><td> 58.7 </td><td> 60.2 </td><td> 64.4 </td><td> 68.6 </td></tr>
<tr><td>Bentley</td><td>Continental GT</td><td>6.0 V12</td><td>2013</td><td> 48.0 </td><td> 56.1 </td><td> 61.3 </td><td> 63.6 </td><td> 67.2 </td><td> 70.8 </td></tr>
<tr><td>BMW</td><td>1</td><td>118d</td><td>2008</td><td> 49.3 </td><td> 61.1 </td><td> 64.9 </td><td> 65.4 </td><td> 68.4 </td><td> 70.1 </td></tr>
<tr><td>BMW</td><td>1</td><td>120d Coupe</td><td>2008</td><td> 40.8 </td><td> 50.2 </td><td> 57.7 </td><td> 61.4 </td><td> 62.7 </td><td> 64.3 </td></tr>
<tr><td>BMW</td><td>1</td><td>120i Cabrio</td><td>2008</td><td> 49.6 </td><td> 57.2 </td><td> 60.3 </td><td> 63.8 </td><td> 65.6 </td><td> 68.6 </td></tr>
<tr><td>BMW</td><td>1</td><td>125i Cabrio</td><td>2008</td><td> 46.5 </td><td> 57.2 </td><td> 65.8 </td><td> 68.2 </td><td> 71.6 </td><td> 75.4 </td></tr>
<tr><td>BMW</td><td>1</td><td>128i</td><td>2008</td><td> 47.3 </td><td> 56.8 </td><td> 62.8 </td><td> 65.9 </td><td> 68.6 </td><td> 71.4 </td></tr>
<tr><td>BMW</td><td>1</td><td>135i Cabrio</td><td>2008</td><td> 66.7 </td><td> 67.6 </td><td> 68.3 </td><td> 68.3 </td><td> 69.4 </td><td> 70.5 </td></tr>
<tr><td>BMW</td><td>1</td><td>135i Coupe</td><td>2008</td><td> 48.1 </td><td> 58.0 </td><td> 64.1 </td><td> 67.3 </td><td> 69.9 </td><td> 72.5 </td></tr>
<tr><td>BMW</td><td>1</td><td>135i Coupe</td><td>2009</td><td> 43.8 </td><td> 53.9 </td><td> 62.0 </td><td> 65.0 </td><td> 67.5 </td><td> 70.2 </td></tr>
<tr><td>BMW</td><td>1</td><td>118i</td><td>2010</td><td> 40.6 </td><td> 60.5 </td><td> 64.0 </td><td> 66.5 </td><td> 68.5 </td><td> 70.9 </td></tr>
<tr><td>BMW</td><td>1</td><td>118i Cabrio</td><td>2010</td><td> 36.6 </td><td> 60.6 </td><td> 63.1 </td><td> 66.0 </td><td> 69.4 </td><td> 71.8 </td></tr>
<tr><td>BMW</td><td>1</td><td>116i</td><td>2011</td><td> 43.6 </td><td> 61.1 </td><td> 64.5 </td><td> 67.0 </td><td> 69.0 </td><td> 74.5 </td></tr>
<tr><td>BMW</td><td>1</td><td>118d</td><td>2011</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 66.5 </td><td> 68.0 </td><td> 69.9 </td></tr>
<tr><td>BMW</td><td>1</td><td>118i</td><td>2011</td><td> 40.7 </td><td> 57.3 </td><td> 60.7 </td><td> 63.4 </td><td> 66.1 </td><td> 69.8 </td></tr>
<tr><td>BMW</td><td>1</td><td>1M</td><td>2011</td><td> 48.5 </td><td> 59.9 </td><td> 66.8 </td><td> 70.9 </td><td> 72.7 </td><td> 74.5 </td></tr>
<tr><td>BMW</td><td>1</td><td>116i</td><td>2012</td><td> 39.6 </td><td> 57.9 </td><td> 61.5 </td><td> 63.2 </td><td> 65.7 </td><td> 67.5 </td></tr>
<tr><td>BMW</td><td>1</td><td>125d</td><td>2012</td><td> 47.1 </td><td> 55.7 </td><td> 60.1 </td><td> 63.8 </td><td> 67.4 </td><td> 69.7 </td></tr>
<tr><td>BMW</td><td>1</td><td>125i</td><td>2012</td><td> 45.5 </td><td> 57.2 </td><td> 62.5 </td><td> 65.8 </td><td> 69.4 </td><td> 71.3 </td></tr>
<tr><td>BMW</td><td>1</td><td>114i</td><td>2013</td><td> 42.4 </td><td> 57.4 </td><td> 62.3 </td><td> 64.7 </td><td> 67.8 </td><td> 70.5 </td></tr>
<tr><td>BMW</td><td>1</td><td>116d</td><td>2013</td><td> 43.2 </td><td> 53.1 </td><td> 61.1 </td><td> 64.1 </td><td> 66.5 </td><td> 69.1 </td></tr>
<tr><td>BMW</td><td>1</td><td>116i</td><td>2013</td><td> 43.2 </td><td> 53.2 </td><td> 61.2 </td><td> 64.1 </td><td> 66.6 </td><td> 69.4 </td></tr>
<tr><td>BMW</td><td>1</td><td>125d</td><td>2013</td><td> 42.8 </td><td> 52.7 </td><td> 60.6 </td><td> 64.1 </td><td> 65.9 </td><td> 68.1 </td></tr>
<tr><td>BMW</td><td>1</td><td>135i</td><td>2013</td><td> 42.9 </td><td> 52.8 </td><td> 60.7 </td><td> 64.9 </td><td> 66.0 </td><td> 67.5 </td></tr>
<tr><td>BMW</td><td>1</td><td>116i</td><td>2015</td><td> 42.4 </td><td> 57.6 </td><td> 61.8 </td><td> 64.9 </td><td> 67.6 </td><td> 71.3 </td></tr>
<tr><td>BMW</td><td>1</td><td>116i</td><td>2016</td><td> 41.9 </td><td> 56.8 </td><td> 60.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>BMW</td><td>1</td><td>118i</td><td>2017</td><td> 44.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>BMW</td><td>1</td><td>120i</td><td>2017</td><td> 37.7 </td><td> 53.8 </td><td> 59.9 </td><td> 63.4 </td><td> 70.1 </td><td> 70.2 </td></tr>
<tr><td>BMW</td><td>1</td><td>140i</td><td>2017</td><td> 45.9 </td><td> 61.8 </td><td> 64.0 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>BMW</td><td>2</td><td>218i</td><td>2014</td><td> 44.5 </td><td> 57.7 </td><td> 62.2 </td><td> 64.9 </td><td> 68.6 </td><td> 71.8 </td></tr>
<tr><td>BMW</td><td>2</td><td>218D Gran Tourer</td><td>2015</td><td> 42.9 </td><td> 59.2 </td><td> 62.6 </td><td> 65.9 </td><td> 69.6 </td><td> 71.3 </td></tr>
<tr><td>BMW</td><td>2</td><td>220D Cabrio</td><td>2015</td><td> 42.3 </td><td> 58.2 </td><td> 61.6 </td><td> 64.9 </td><td> 70.6 </td><td> 72.3 </td></tr>
<tr><td>BMW</td><td>2</td><td>220i</td><td>2015</td><td> 39.3 </td><td> 58.5 </td><td> 62.5 </td><td> 66.6 </td><td> 69.3 </td><td> 73.6 </td></tr>
<tr><td>BMW</td><td>2</td><td>225i</td><td>2015</td><td> 42.9 </td><td> 60.2 </td><td> 63.1 </td><td> 65.9 </td><td> 68.6 </td><td> 70.3 </td></tr>
<tr><td>BMW</td><td>2</td><td>218i Active Tourer</td><td>2016</td><td> 39.9 </td><td> 59.8 </td><td> 63.0 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>BMW</td><td>2</td><td>220d Gran Tourer</td><td>2016</td><td> 46.1 </td><td> 61.2 </td><td> 63.8 </td><td> 66.3 </td><td> 68.3 </td><td> 71.8 </td></tr>
<tr><td>BMW</td><td>2</td><td>216d</td><td>2017</td><td> 47.9 </td><td> 59.8 </td><td> 63.0 </td><td> 66.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>BMW</td><td>3</td><td>318d</td><td>2008</td><td> 46.6 </td><td> 59.0 </td><td> 62.0 </td><td> 64.0 </td><td> 67.0 </td><td> 70.0 </td></tr>
<tr><td>BMW</td><td>3</td><td>320d</td><td>2008</td><td> 43.7 </td><td> 53.8 </td><td> 61.8 </td><td> 65.5 </td><td> 67.2 </td><td> 69.3 </td></tr>
<tr><td>BMW</td><td>3</td><td>320i</td><td>2008</td><td> 43.9 </td><td> 63.7 </td><td> 66.9 </td><td> 67.7 </td><td> 70.9 </td><td> 72.7 </td></tr>
<tr><td>BMW</td><td>3</td><td>325i</td><td>2008</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 65.5 </td><td> 69.1 </td><td> 73.2 </td></tr>
<tr><td>BMW</td><td>3</td><td>325i Coupe</td><td>2009</td><td> 41.6 </td><td> 60.0 </td><td> 64.0 </td><td> 65.5 </td><td> 68.0 </td><td> 70.0 </td></tr>
<tr><td>BMW</td><td>3</td><td>330d</td><td>2009</td><td> 42.6 </td><td> 52.5 </td><td> 60.4 </td><td> 64.5 </td><td> 65.6 </td><td> 67.1 </td></tr>
<tr><td>BMW</td><td>3</td><td>335d</td><td>2009</td><td> 46.4 </td><td> 55.0 </td><td> 60.4 </td><td> 63.1 </td><td> 65.7 </td><td> 68.3 </td></tr>
<tr><td>BMW</td><td>3</td><td>335i Coupe</td><td>2009</td><td> 50.1 </td><td> 62.5 </td><td> 66.0 </td><td> 67.9 </td><td> 70.6 </td><td> 73.0 </td></tr>
<tr><td>BMW</td><td>3</td><td>325i Cabrio</td><td>2010</td><td> 43.3 </td><td> 59.0 </td><td> 64.5 </td><td> 66.3 </td><td> 69.1 </td><td> 71.2 </td></tr>
<tr><td>BMW</td><td>3</td><td>320d Stationcar</td><td>2011</td><td> 50.3 </td><td> 57.8 </td><td> 63.1 </td><td> 66.7 </td><td> 68.3 </td><td> 71.7 </td></tr>
<tr><td>BMW</td><td>3</td><td>320i Coupe</td><td>2011</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 65.5 </td><td> 68.1 </td><td> 71.1 </td></tr>
<tr><td>BMW</td><td>3</td><td>320d</td><td>2012</td><td> 43.5 </td><td> 57.4 </td><td> 60.5 </td><td> 63.3 </td><td> 66.9 </td><td> 70.8 </td></tr>
<tr><td>BMW</td><td>3</td><td>320i</td><td>2012</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 64.7 </td><td> 68.1 </td><td> 71.9 </td></tr>
<tr><td>BMW</td><td>3</td><td>328i</td><td>2012</td><td> 42.0 </td><td> 53.6 </td><td> 60.8 </td><td> 64.8 </td><td> 67.3 </td><td> 69.8 </td></tr>
<tr><td>BMW</td><td>3</td><td>328i</td><td>2012</td><td> 44.0 </td><td> 54.2 </td><td> 62.3 </td><td> 64.9 </td><td> 67.8 </td><td> 71.1 </td></tr>
<tr><td>BMW</td><td>3</td><td>320i</td><td>2013</td><td> 40.6 </td><td> 55.8 </td><td> 59.2 </td><td> 63.6 </td><td> 66.5 </td><td> 70.6 </td></tr>
<tr><td>BMW</td><td>3</td><td>320d</td><td>2014</td><td> 44.9 </td><td> 55.8 </td><td> 59.8 </td><td> 62.9 </td><td> 66.6 </td><td> 69.2 </td></tr>
<tr><td>BMW</td><td>3</td><td>320d Stationcar</td><td>2014</td><td> 41.0 </td><td> 55.2 </td><td> 59.1 </td><td> 62.9 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>BMW</td><td>3</td><td>330d Stationcar</td><td>2014</td><td> 41.0 </td><td> 59.2 </td><td> 61.1 </td><td> 62.9 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>BMW</td><td>3</td><td>316 Stationcar</td><td>2015</td><td> 46.1 </td><td> 57.0 </td><td> 61.6 </td><td> 64.5 </td><td> 66.7 </td><td> 69.5 </td></tr>
<tr><td>BMW</td><td>3</td><td>320d</td><td>2016</td><td> 42.9 </td><td> 56.2 </td><td> 59.9 </td><td> 63.0 </td><td> 67.4 </td><td> 69.5 </td></tr>
<tr><td>BMW</td><td>3</td><td>320i</td><td>2016</td><td> 40.1 </td><td> 58.2 </td><td> 61.2 </td><td> 64.3 </td><td> 66.3 </td><td> 69.7 </td></tr>
<tr><td>BMW</td><td>3</td><td>320d</td><td>2017</td><td> 43.9 </td><td> 58.8 </td><td> 61.5 </td><td> 64.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>BMW</td><td>4</td><td>428i</td><td>2014</td><td> 42.4 </td><td> 52.7 </td><td> 59.1 </td><td> 62.4 </td><td> 65.4 </td><td> 68.3 </td></tr>
<tr><td>BMW</td><td>4</td><td>430i</td><td>2016</td><td> 44.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>BMW</td><td>4</td><td>430i Gran Coupe</td><td>2017</td><td> 40.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>BMW</td><td>5</td><td>530d</td><td>2008</td><td> 46.2 </td><td> 56.6 </td><td> 60.1 </td><td> 64.1 </td><td> 66.6 </td><td> 71.1 </td></tr>
<tr><td>BMW</td><td>5</td><td>535i</td><td>2008</td><td> 43.6 </td><td> 52.2 </td><td> 57.6 </td><td> 60.3 </td><td> 63.1 </td><td> 66.0 </td></tr>
<tr><td>BMW</td><td>5</td><td>530d GT</td><td>2009</td><td> 43.1 </td><td> 56.2 </td><td> 60.5 </td><td> 64.2 </td><td> 66.5 </td><td> 69.1 </td></tr>
<tr><td>BMW</td><td>5</td><td>523i</td><td>2010</td><td> 42.4 </td><td> 52.2 </td><td> 60.0 </td><td> 63.8 </td><td> 65.2 </td><td> 67.0 </td></tr>
<tr><td>BMW</td><td>5</td><td>530d</td><td>2010</td><td> 44.6 </td><td> 56.7 </td><td> 61.1 </td><td> 62.9 </td><td> 65.1 </td><td> 68.8 </td></tr>
<tr><td>BMW</td><td>5</td><td>535i GT</td><td>2010</td><td> 42.9 </td><td> 52.8 </td><td> 60.7 </td><td> 63.6 </td><td> 66.1 </td><td> 68.8 </td></tr>
<tr><td>BMW</td><td>5</td><td>550i GT</td><td>2010</td><td> 34.5 </td><td> 48.2 </td><td> 56.8 </td><td> 61.3 </td><td> 65.2 </td><td> 69.1 </td></tr>
<tr><td>BMW</td><td>5</td><td>520d Stationcar</td><td>2011</td><td> 43.5 </td><td> 53.5 </td><td> 61.5 </td><td> 64.5 </td><td> 67.0 </td><td> 69.8 </td></tr>
<tr><td>BMW</td><td>5</td><td>530d</td><td>2011</td><td> 44.6 </td><td> 56.7 </td><td> 61.1 </td><td> 62.9 </td><td> 65.1 </td><td> 68.9 </td></tr>
<tr><td>BMW</td><td>5</td><td>535i</td><td>2011</td><td> 42.6 </td><td> 54.7 </td><td> 62.1 </td><td> 66.4 </td><td> 68.3 </td><td> 70.2 </td></tr>
<tr><td>BMW</td><td>5</td><td>535i Stationcar</td><td>2011</td><td> 40.9 </td><td> 55.9 </td><td> 59.2 </td><td> 62.6 </td><td> 65.6 </td><td> 67.8 </td></tr>
<tr><td>BMW</td><td>5</td><td>535i</td><td>2012</td><td> 42.8 </td><td> 52.0 </td><td> 57.8 </td><td> 60.9 </td><td> 63.1 </td><td> 65.4 </td></tr>
<tr><td>BMW</td><td>5</td><td>ActiveHybrid</td><td>2012</td><td> 41.8 </td><td> 53.5 </td><td> 58.4 </td><td> 61.3 </td><td> 65.2 </td><td> 68.1 </td></tr>
<tr><td>BMW</td><td>5</td><td>ActiveHybrid</td><td>2012</td><td> 41.3 </td><td> 50.8 </td><td> 58.4 </td><td> 61.8 </td><td> 63.5 </td><td> 65.6 </td></tr>
<tr><td>BMW</td><td>5</td><td>520i Stationcar</td><td>2015</td><td> 42.9 </td><td> 60.2 </td><td> 63.1 </td><td> 65.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>BMW</td><td>5</td><td>530d</td><td>2015</td><td> 41.0 </td><td> 55.2 </td><td> 59.1 </td><td> 62.9 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>BMW</td><td>5</td><td>520d</td><td>2016</td><td> 45.9 </td><td> 57.8 </td><td> 60.5 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>BMW</td><td>5</td><td>520d Stationcar</td><td>2016</td><td> 43.9 </td><td> 57.8 </td><td> 61.5 </td><td> 64.7 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>BMW</td><td>5</td><td>530d</td><td>2016</td><td> 41.9 </td><td> 56.8 </td><td> 60.5 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>BMW</td><td>5</td><td>535d</td><td>2016</td><td> 46.9 </td><td> 57.8 </td><td> 60.5 </td><td> 63.3 </td><td> 65.1 </td><td> 68.2 </td></tr>
<tr><td>BMW</td><td>5</td><td>530d</td><td>2017</td><td> 41.9 </td><td> 55.8 </td><td> 59.0 </td><td> 62.2 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>BMW</td><td>5</td><td>530d stationcar</td><td>2017</td><td> 41.9 </td><td> 55.8 </td><td> 59.5 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>BMW</td><td>5</td><td>530i</td><td>2017</td><td> 37.9 </td><td> 54.8 </td><td> 58.5 </td><td> 61.2 </td><td> 62.3 </td><td> 65.5 </td></tr>
<tr><td>BMW</td><td>5</td><td>530i stationcar</td><td>2017</td><td> 37.1 </td><td> 51.7 </td><td> 57.5 </td><td> 59.6 </td><td> 65.5 </td><td> 65.6 </td></tr>
<tr><td>BMW</td><td>5</td><td>540i</td><td>2017</td><td> 38.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>BMW</td><td>6</td><td>640i Gran Coupe</td><td>2012</td><td> 41.6 </td><td> 51.2 </td><td> 58.9 </td><td> 63.2 </td><td> 64.0 </td><td> 65.1 </td></tr>
<tr><td>BMW</td><td>6</td><td>650i</td><td>2012</td><td> 47.3 </td><td> 55.0 </td><td> 60.0 </td><td> 62.1 </td><td> 65.7 </td><td> 69.3 </td></tr>
<tr><td>BMW</td><td>6</td><td>650i</td><td>2012</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 65.2 </td><td> 67.1 </td><td> 69.4 </td></tr>
<tr><td>BMW</td><td>7</td><td>730d</td><td>2009</td><td> 42.1 </td><td> 56.3 </td><td> 60.1 </td><td> 62.0 </td><td> 66.7 </td><td> 68.1 </td></tr>
<tr><td>BMW</td><td>7</td><td>750i</td><td>2009</td><td> 41.4 </td><td> 53.9 </td><td> 61.6 </td><td> 66.0 </td><td> 68.1 </td><td> 70.2 </td></tr>
<tr><td>BMW</td><td>7</td><td>740d</td><td>2010</td><td> 42.4 </td><td> 52.2 </td><td> 60.0 </td><td> 63.8 </td><td> 65.2 </td><td> 67.0 </td></tr>
<tr><td>BMW</td><td>7</td><td>750iL</td><td>2010</td><td> 38.5 </td><td> 56.1 </td><td> 61.2 </td><td> 63.0 </td><td> 64.8 </td><td> 67.0 </td></tr>
<tr><td>BMW</td><td>7</td><td>740i</td><td>2011</td><td> 44.8 </td><td> 53.7 </td><td> 59.3 </td><td> 62.0 </td><td> 65.0 </td><td> 68.1 </td></tr>
<tr><td>BMW</td><td>7</td><td>750i</td><td>2013</td><td> 40.3 </td><td> 55.2 </td><td> 58.6 </td><td> 61.9 </td><td> 65.7 </td><td> 67.3 </td></tr>
<tr><td>BMW</td><td>7</td><td>730d</td><td>2014</td><td> 39.7 </td><td> 56.2 </td><td> 58.6 </td><td> 60.9 </td><td> 65.7 </td><td> 67.3 </td></tr>
<tr><td>BMW</td><td>7</td><td>730d</td><td>2016</td><td> 42.9 </td><td> 53.9 </td><td> 57.7 </td><td> 60.5 </td><td> 63.0 </td><td> 66.0 </td></tr>
<tr><td>BMW</td><td>7</td><td>760i</td><td>2017</td><td> 35.9 </td><td> 57.8 </td><td> 59.0 </td><td> 60.2 </td><td> 62.3 </td><td> 65.5 </td></tr>
<tr><td>BMW</td><td>i3</td><td>&nbsp;</td><td>2014</td><td> 43.4 </td><td> 53.5 </td><td> 59.8 </td><td> 64.2 </td><td> 66.9 </td><td> 71.4 </td></tr>
<tr><td>BMW</td><td>i3</td><td>&nbsp;</td><td>2017</td><td> 45.5 </td><td> 55.1 </td><td> 58.9 </td><td> 62.9 </td><td> 70.1 </td><td> 70.2 </td></tr>
<tr><td>BMW</td><td>i8</td><td>&nbsp;</td><td>2014</td><td> 42.3 </td><td> 60.2 </td><td> 62.6 </td><td> 64.9 </td><td> 70.6 </td><td> 72.3 </td></tr>
<tr><td>BMW</td><td>M2</td><td>&nbsp;</td><td>2016</td><td> 49.9 </td><td> 61.8 </td><td> 64.5 </td><td> 67.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>BMW</td><td>M2</td><td>&nbsp;</td><td>2017</td><td> 44.9 </td><td> 61.8 </td><td> 65.5 </td><td> 69.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>BMW</td><td>M3</td><td>&nbsp;</td><td>2008</td><td> 51.1 </td><td> 61.1 </td><td> 67.3 </td><td> 70.4 </td><td> 73.7 </td><td> 77.0 </td></tr>
<tr><td>BMW</td><td>M3</td><td>Cabrio</td><td>2008</td><td> 53.4 </td><td> 62.7 </td><td> 68.6 </td><td> 71.6 </td><td> 74.3 </td><td> 77.0 </td></tr>
<tr><td>BMW</td><td>M3</td><td>&nbsp;</td><td>2013</td><td> 48.0 </td><td> 58.2 </td><td> 64.7 </td><td> 67.9 </td><td> 71.2 </td><td> 74.5 </td></tr>
<tr><td>BMW</td><td>M3</td><td>&nbsp;</td><td>2014</td><td> 44.9 </td><td> 60.2 </td><td> 64.6 </td><td> 68.9 </td><td> 71.5 </td><td> 73.3 </td></tr>
<tr><td>BMW</td><td>M3</td><td>&nbsp;</td><td>2017</td><td> 48.9 </td><td> 62.7 </td><td> 65.5 </td><td> 68.3 </td><td> 72.1 </td><td> 75.8 </td></tr>
<tr><td>BMW</td><td>M4</td><td>&nbsp;</td><td>2017</td><td> 46.9 </td><td> 64.7 </td><td> 67.0 </td><td> 67.9 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>BMW</td><td>M4</td><td>CS</td><td>2017</td><td> 45.9 </td><td> 62.7 </td><td> 66.5 </td><td> 70.3 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>BMW</td><td>M5</td><td>&nbsp;</td><td>2012</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 65.7 </td><td> 68.4 </td><td> 71.5 </td></tr>
<tr><td>BMW</td><td>M6</td><td>Cabrio</td><td>2012</td><td> 48.8 </td><td> 56.3 </td><td> 61.3 </td><td> 62.9 </td><td> 68.2 </td><td> 73.6 </td></tr>
<tr><td>BMW</td><td>M6</td><td>&nbsp;</td><td>2017</td><td> 44.9 </td><td> 59.8 </td><td> 63.0 </td><td> 66.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>BMW</td><td>X1</td><td>xDrive 20d</td><td>2011</td><td> 44.5 </td><td> 59.5 </td><td> 62.4 </td><td> 65.5 </td><td> 68.5 </td><td> 71.0 </td></tr>
<tr><td>BMW</td><td>X1</td><td>Xdrive 28i</td><td>2011</td><td> 42.9 </td><td> 52.8 </td><td> 60.7 </td><td> 64.7 </td><td> 66.0 </td><td> 67.7 </td></tr>
<tr><td>BMW</td><td>X1</td><td>xDrive 30i</td><td>2013</td><td> 48.8 </td><td> 56.2 </td><td> 60.9 </td><td> 63.1 </td><td> 65.9 </td><td> 68.7 </td></tr>
<tr><td>BMW</td><td>X1</td><td>xDrive 28i</td><td>2015</td><td> 42.9 </td><td> 59.2 </td><td> 62.6 </td><td> 65.9 </td><td> 68.6 </td><td> 70.3 </td></tr>
<tr><td>BMW</td><td>X1</td><td>xDrive 20d</td><td>2016</td><td> 45.1 </td><td> 58.2 </td><td> 61.7 </td><td> 65.3 </td><td> 67.3 </td><td> 70.7 </td></tr>
<tr><td>BMW</td><td>X1</td><td>sDrive18i</td><td>2017</td><td> 43.9 </td><td> 56.8 </td><td> 60.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>BMW</td><td>X3</td><td>xDrive 30i</td><td>2008</td><td> 42.2 </td><td> 51.9 </td><td> 59.7 </td><td> 64.5 </td><td> 64.9 </td><td> 65.6 </td></tr>
<tr><td>BMW</td><td>X3</td><td>xDrive 35d</td><td>2008</td><td> 41.8 </td><td> 57.1 </td><td> 61.3 </td><td> 64.6 </td><td> 68.1 </td><td> 70.2 </td></tr>
<tr><td>BMW</td><td>X3</td><td>xDrive 20d</td><td>2011</td><td> 46.2 </td><td> 58.2 </td><td> 62.1 </td><td> 65.3 </td><td> 69.1 </td><td> 72.4 </td></tr>
<tr><td>BMW</td><td>X3</td><td>xDrive 35i</td><td>2011</td><td> 44.0 </td><td> 54.1 </td><td> 60.5 </td><td> 63.3 </td><td> 67.7 </td><td> 72.1 </td></tr>
<tr><td>BMW</td><td>X3</td><td>xDrive 20d</td><td>2014</td><td> 41.2 </td><td> 57.2 </td><td> 60.6 </td><td> 63.8 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>BMW</td><td>X3</td><td>xDrive 20d</td><td>2016</td><td> 48.1 </td><td> 61.2 </td><td> 62.8 </td><td> 64.3 </td><td> 65.3 </td><td> 68.7 </td></tr>
<tr><td>BMW</td><td>X3</td><td>xDrive 35d</td><td>2016</td><td> 45.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>BMW</td><td>X3</td><td>xDrive20d</td><td>2017</td><td> 48.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>BMW</td><td>X4</td><td>xDrive 35d</td><td>2014</td><td> 41.6 </td><td> 57.4 </td><td> 60.7 </td><td> 63.9 </td><td> 66.7 </td><td> 68.4 </td></tr>
<tr><td>BMW</td><td>X4</td><td>xDrive 35i</td><td>2015</td><td> 41.3 </td><td> 56.3 </td><td> 61.8 </td><td> 64.9 </td><td> 67.9 </td><td> 71.2 </td></tr>
<tr><td>BMW</td><td>X4</td><td>xDrive 30d</td><td>2016</td><td> 47.9 </td><td> 57.8 </td><td> 60.5 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>BMW</td><td>X5</td><td>M</td><td>2010</td><td> 43.0 </td><td> 51.9 </td><td> 57.6 </td><td> 59.9 </td><td> 64.7 </td><td> 69.5 </td></tr>
<tr><td>BMW</td><td>X5</td><td>xDrive 30d</td><td>2010</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 65.1 </td><td> 68.3 </td><td> 71.9 </td></tr>
<tr><td>BMW</td><td>X5</td><td>xDrive 30d</td><td>2012</td><td> 43.2 </td><td> 55.5 </td><td> 60.1 </td><td> 63.3 </td><td> 66.6 </td><td> 70.2 </td></tr>
<tr><td>BMW</td><td>X5</td><td>xDrive 30d</td><td>2012</td><td> 42.6 </td><td> 52.5 </td><td> 60.4 </td><td> 63.4 </td><td> 65.7 </td><td> 68.2 </td></tr>
<tr><td>BMW</td><td>X5</td><td>xDrive 30d</td><td>2013</td><td> 41.4 </td><td> 56.3 </td><td> 58.0 </td><td> 60.8 </td><td> 64.6 </td><td> 68.2 </td></tr>
<tr><td>BMW</td><td>X5</td><td>3.0 V6</td><td>2014</td><td> 40.3 </td><td> 50.7 </td><td> 57.2 </td><td> 60.5 </td><td> 63.5 </td><td> 66.5 </td></tr>
<tr><td>BMW</td><td>X5</td><td>xDrive 30d</td><td>2014</td><td> 41.6 </td><td> 56.2 </td><td> 60.1 </td><td> 63.9 </td><td> 65.7 </td><td> 67.3 </td></tr>
<tr><td>BMW</td><td>X5</td><td>xDrive 50i</td><td>2014</td><td> 46.1 </td><td> 55.2 </td><td> 58.2 </td><td> 61.2 </td><td> 64.4 </td><td> 67.7 </td></tr>
<tr><td>BMW</td><td>X5</td><td>xDrive 30d</td><td>2015</td><td> 41.6 </td><td> 56.2 </td><td> 60.1 </td><td> 63.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>BMW</td><td>X5</td><td>xDrive40e</td><td>2016</td><td> 36.5 </td><td> 51.6 </td><td> 56.9 </td><td> 60.9 </td><td> 64.8 </td><td> 66.9 </td></tr>
<tr><td>BMW</td><td>X6</td><td>xDrive 35i</td><td>2008</td><td> 42.2 </td><td> 54.4 </td><td> 62.0 </td><td> 66.3 </td><td> 68.4 </td><td> 70.6 </td></tr>
<tr><td>BMW</td><td>X6</td><td>xDrive 35d</td><td>2009</td><td> 46.4 </td><td> 57.6 </td><td> 61.4 </td><td> 64.5 </td><td> 67.4 </td><td> 70.3 </td></tr>
<tr><td>BMW</td><td>X6</td><td>xDrive 35i</td><td>2016</td><td> 45.3 </td><td> 56.1 </td><td> 62.7 </td><td> 66.3 </td><td> 68.9 </td><td> 71.6 </td></tr>
<tr><td>BMW</td><td>Z4</td><td>sDrive 35i</td><td>2009</td><td> 48.4 </td><td> 58.4 </td><td> 64.7 </td><td> 67.9 </td><td> 70.9 </td><td> 74.0 </td></tr>
<tr><td>BMW</td><td>Z4</td><td>sDrive 35is</td><td>2011</td><td> 48.9 </td><td> 59.3 </td><td> 65.8 </td><td> 69.1 </td><td> 72.2 </td><td> 75.3 </td></tr>
<tr><td>Buick</td><td>Cascada</td><td>1.6 cabrio</td><td>2016</td><td> 44.2 </td><td> 57.0 </td><td> 64.7 </td><td> 69.6 </td><td> 70.5 </td><td> 71.5 </td></tr>
<tr><td>Buick</td><td>Enclave</td><td>3.6 V6</td><td>2008</td><td> 44.3 </td><td> 55.5 </td><td> 62.4 </td><td> 66.3 </td><td> 68.4 </td><td> 70.4 </td></tr>
<tr><td>Buick</td><td>Enclave</td><td>3.6 V6</td><td>2012</td><td> 43.1 </td><td> 52.7 </td><td> 58.7 </td><td> 62.0 </td><td> 64.1 </td><td> 66.2 </td></tr>
<tr><td>Buick</td><td>Enclave</td><td>3.6 V6</td><td>2016</td><td> 41.9 </td><td> 52.0 </td><td> 58.3 </td><td> 61.8 </td><td> 63.9 </td><td> 66.0 </td></tr>
<tr><td>Buick</td><td>LaCrosse</td><td>CXS</td><td>2010</td><td> 44.9 </td><td> 56.3 </td><td> 63.4 </td><td> 67.1 </td><td> 70.1 </td><td> 73.2 </td></tr>
<tr><td>Buick</td><td>LaCrosse</td><td>3.6 V6</td><td>2013</td><td> 41.4 </td><td> 50.7 </td><td> 56.6 </td><td> 59.4 </td><td> 62.7 </td><td> 66.1 </td></tr>
<tr><td>Buick</td><td>Regal</td><td>CXL 2.4</td><td>2011</td><td> 44.5 </td><td> 54.9 </td><td> 61.3 </td><td> 64.9 </td><td> 67.0 </td><td> 69.1 </td></tr>
<tr><td>Buick</td><td>Verano</td><td>2.4</td><td>2012</td><td> 44.0 </td><td> 54.5 </td><td> 60.8 </td><td> 64.7 </td><td> 65.9 </td><td> 67.2 </td></tr>
<tr><td>Buick</td><td>Verano</td><td>Turbo</td><td>2012</td><td> 41.2 </td><td> 51.3 </td><td> 57.6 </td><td> 61.0 </td><td> 63.5 </td><td> 66.0 </td></tr>
<tr><td>Cadillac</td><td>ATS</td><td>Turbo</td><td>2012</td><td> 41.7 </td><td> 53.6 </td><td> 61.0 </td><td> 65.0 </td><td> 67.6 </td><td> 70.3 </td></tr>
<tr><td>Cadillac</td><td>ATS</td><td>2.0</td><td>2013</td><td> 44.0 </td><td> 54.3 </td><td> 60.7 </td><td> 64.4 </td><td> 66.0 </td><td> 67.6 </td></tr>
<tr><td>Cadillac</td><td>ATX</td><td>3.6 V6</td><td>2012</td><td> 45.6 </td><td> 53.8 </td><td> 59.2 </td><td> 61.0 </td><td> 66.5 </td><td> 72.0 </td></tr>
<tr><td>Cadillac</td><td>BLS</td><td>1.9d Stationcar</td><td>2008</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 65.1 </td><td> 67.2 </td><td> 69.5 </td></tr>
<tr><td>Cadillac</td><td>CTS</td><td>3.6</td><td>2008</td><td> 40.6 </td><td> 57.5 </td><td> 63.0 </td><td> 64.0 </td><td> 65.5 </td><td> 68.0 </td></tr>
<tr><td>Cadillac</td><td>CTS</td><td>3.6 V6</td><td>2008</td><td> 44.1 </td><td> 55.4 </td><td> 62.7 </td><td> 66.0 </td><td> 70.6 </td><td> 75.2 </td></tr>
<tr><td>Cadillac</td><td>CTS</td><td>Stationcar</td><td>2010</td><td> 42.2 </td><td> 50.7 </td><td> 56.2 </td><td> 58.7 </td><td> 62.0 </td><td> 65.3 </td></tr>
<tr><td>Cadillac</td><td>CTS</td><td>3.6 Stationcar</td><td>2011</td><td> 40.7 </td><td> 57.1 </td><td> 62.1 </td><td> 65.4 </td><td> 67.3 </td><td> 69.9 </td></tr>
<tr><td>Cadillac</td><td>CTS</td><td>3.6</td><td>2012</td><td> 42.4 </td><td> 52.2 </td><td> 60.1 </td><td> 64.7 </td><td> 65.3 </td><td> 66.2 </td></tr>
<tr><td>Cadillac</td><td>CTS</td><td>3.6 V6</td><td>2013</td><td> 46.7 </td><td> 54.5 </td><td> 59.8 </td><td> 61.2 </td><td> 67.5 </td><td> 73.9 </td></tr>
<tr><td>Cadillac</td><td>CTS</td><td>3.6 V6</td><td>2015</td><td> 42.3 </td><td> 58.2 </td><td> 61.6 </td><td> 64.9 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>Cadillac</td><td>CTS</td><td>2.0</td><td>2016</td><td> 44.2 </td><td> 55.1 </td><td> 60.1 </td><td> 62.6 </td><td> 65.1 </td><td> 68.1 </td></tr>
<tr><td>Cadillac</td><td>CTS Coupe</td><td>3.6 V6</td><td>2011</td><td> 44.3 </td><td> 56.0 </td><td> 63.3 </td><td> 67.4 </td><td> 69.5 </td><td> 71.6 </td></tr>
<tr><td>Cadillac</td><td>CTS-V</td><td>Hennessey</td><td>2010</td><td> 58.4 </td><td> 64.8 </td><td> 69.2 </td><td> 70.1 </td><td> 76.1 </td><td> 82.2 </td></tr>
<tr><td>Cadillac</td><td>CTS-V</td><td>Stationcar</td><td>2011</td><td> 50.0 </td><td> 58.4 </td><td> 63.7 </td><td> 66.3 </td><td> 69.0 </td><td> 71.6 </td></tr>
<tr><td>Cadillac</td><td>CTS-V</td><td>6.2 V8</td><td>2012</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 66.7 </td><td> 68.5 </td><td> 70.7 </td></tr>
<tr><td>Cadillac</td><td>CTS-V</td><td>&nbsp;</td><td>2017</td><td> 45.9 </td><td> 60.8 </td><td> 63.5 </td><td> 64.9 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Cadillac</td><td>Escalade</td><td>Hybrid</td><td>2009</td><td> 48.3 </td><td> 58.6 </td><td> 64.9 </td><td> 68.7 </td><td> 69.9 </td><td> 71.2 </td></tr>
<tr><td>Cadillac</td><td>Escalade</td><td>6.2 V8</td><td>2016</td><td> 38.4 </td><td> 52.3 </td><td> 60.7 </td><td> 65.8 </td><td> 67.2 </td><td> 68.6 </td></tr>
<tr><td>Cadillac</td><td>SRX</td><td>2.8 V6 Turbo</td><td>2010</td><td> 43.3 </td><td> 55.5 </td><td> 63.0 </td><td> 67.5 </td><td> 69.0 </td><td> 70.6 </td></tr>
<tr><td>Cadillac</td><td>SRX</td><td>3.0 V6</td><td>2010</td><td> 42.8 </td><td> 55.9 </td><td> 63.9 </td><td> 68.5 </td><td> 70.9 </td><td> 73.3 </td></tr>
<tr><td>Cadillac</td><td>XT5</td><td>3.6 V6</td><td>2017</td><td> 43.9 </td><td> 55.8 </td><td> 59.5 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Chevrolet</td><td>Aveo</td><td>1.2</td><td>2008</td><td> 48.0 </td><td> 59.1 </td><td> 68.0 </td><td> 70.9 </td><td> 74.0 </td><td> 77.5 </td></tr>
<tr><td>Chevrolet</td><td>Aveo</td><td>1.4 LT</td><td>2011</td><td> 42.1 </td><td> 59.9 </td><td> 64.6 </td><td> 66.8 </td><td> 70.9 </td><td> 73.4 </td></tr>
<tr><td>Chevrolet</td><td>Camaro</td><td>2LT V6</td><td>2010</td><td> 43.0 </td><td> 52.2 </td><td> 58.1 </td><td> 60.7 </td><td> 65.0 </td><td> 69.4 </td></tr>
<tr><td>Chevrolet</td><td>Camaro</td><td>Callaway</td><td>2010</td><td> 55.3 </td><td> 63.6 </td><td> 68.7 </td><td> 71.5 </td><td> 73.3 </td><td> 75.1 </td></tr>
<tr><td>Chevrolet</td><td>Camaro</td><td>SS</td><td>2010</td><td> 53.8 </td><td> 60.6 </td><td> 65.1 </td><td> 66.6 </td><td> 71.1 </td><td> 75.6 </td></tr>
<tr><td>Chevrolet</td><td>Camaro</td><td>SS Cabrio</td><td>2011</td><td> 51.5 </td><td> 59.6 </td><td> 64.9 </td><td> 67.0 </td><td> 71.2 </td><td> 75.4 </td></tr>
<tr><td>Chevrolet</td><td>Camaro</td><td>ZL1</td><td>2011</td><td> 61.2 </td><td> 66.9 </td><td> 70.7 </td><td> 71.8 </td><td> 76.0 </td><td> 80.2 </td></tr>
<tr><td>Chevrolet</td><td>Camaro</td><td>6.2 V8</td><td>2012</td><td> 50.3 </td><td> 59.6 </td><td> 65.5 </td><td> 68.3 </td><td> 71.8 </td><td> 75.3 </td></tr>
<tr><td>Chevrolet</td><td>Camaro</td><td>6.2 V8</td><td>2016</td><td> 48.9 </td><td> 62.7 </td><td> 65.5 </td><td> 68.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Chevrolet</td><td>Camaro</td><td>6.2 V8</td><td>2017</td><td> 46.9 </td><td> 62.7 </td><td> 64.5 </td><td> 66.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Chevrolet</td><td>Captiva</td><td>2.0 VCDI</td><td>2008</td><td> 45.1 </td><td> 55.5 </td><td> 63.8 </td><td> 66.9 </td><td> 69.5 </td><td> 72.5 </td></tr>
<tr><td>Chevrolet</td><td>Cobalt</td><td>SS</td><td>2008</td><td> 49.5 </td><td> 60.0 </td><td> 66.5 </td><td> 70.2 </td><td> 72.1 </td><td> 74.1 </td></tr>
<tr><td>Chevrolet</td><td>Cobalt</td><td>2.2</td><td>2009</td><td> 46.2 </td><td> 58.2 </td><td> 65.6 </td><td> 69.9 </td><td> 71.6 </td><td> 73.3 </td></tr>
<tr><td>Chevrolet</td><td>Corvette</td><td>&nbsp;</td><td>2008</td><td> 61.4 </td><td> 65.8 </td><td> 69.0 </td><td> 69.4 </td><td> 74.5 </td><td> 79.7 </td></tr>
<tr><td>Chevrolet</td><td>Corvette</td><td>ZR1</td><td>2009</td><td> 57.7 </td><td> 65.2 </td><td> 70.2 </td><td> 71.6 </td><td> 77.5 </td><td> 83.4 </td></tr>
<tr><td>Chevrolet</td><td>Corvette</td><td>6.2 V8</td><td>2010</td><td> 53.1 </td><td> 58.3 </td><td> 62.1 </td><td> 62.3 </td><td> 69.1 </td><td> 76.0 </td></tr>
<tr><td>Chevrolet</td><td>Corvette</td><td>ZR1</td><td>2010</td><td> 58.3 </td><td> 66.5 </td><td> 71.9 </td><td> 73.7 </td><td> 79.1 </td><td> 84.4 </td></tr>
<tr><td>Chevrolet</td><td>Corvette</td><td>6.2 V8</td><td>2011</td><td> 57.2 </td><td> 68.3 </td><td> 75.1 </td><td> 79.1 </td><td> 80.9 </td><td> 82.7 </td></tr>
<tr><td>Chevrolet</td><td>Corvette</td><td>ZR1</td><td>2012</td><td> 54.4 </td><td> 60.7 </td><td> 65.1 </td><td> 66.0 </td><td> 72.0 </td><td> 77.9 </td></tr>
<tr><td>Chevrolet</td><td>Corvette</td><td>Stingray</td><td>2013</td><td> 52.6 </td><td> 62.0 </td><td> 68.1 </td><td> 70.5 </td><td> 75.5 </td><td> 80.5 </td></tr>
<tr><td>Chevrolet</td><td>Corvette</td><td>6.2 V8 Convertible</td><td>2016</td><td> 55.8 </td><td> 62.7 </td><td> 66.5 </td><td> 70.3 </td><td> 73.0 </td><td> 76.8 </td></tr>
<tr><td>Chevrolet</td><td>Corvette</td><td>Stingray 6.2 V8</td><td>2017</td><td> 55.8 </td><td> 63.7 </td><td> 67.5 </td><td> 71.3 </td><td> 75.0 </td><td> 78.8 </td></tr>
<tr><td>Chevrolet</td><td>Cruze</td><td>1.8 LT</td><td>2009</td><td> 41.6 </td><td> 60.4 </td><td> 63.4 </td><td> 66.2 </td><td> 69.8 </td><td> 73.7 </td></tr>
<tr><td>Chevrolet</td><td>Cruze</td><td>1.4 turbo</td><td>2012</td><td> 45.6 </td><td> 58.3 </td><td> 63.8 </td><td> 67.9 </td><td> 70.3 </td><td> 74.4 </td></tr>
<tr><td>Chevrolet</td><td>Cruze</td><td>1.8</td><td>2012</td><td> 45.5 </td><td> 61.0 </td><td> 62.3 </td><td> 66.0 </td><td> 70.0 </td><td> 73.5 </td></tr>
<tr><td>Chevrolet</td><td>Equinox</td><td>Fuel Cell</td><td>2008</td><td> 49.8 </td><td> 57.9 </td><td> 62.8 </td><td> 65.9 </td><td> 66.5 </td><td> 67.1 </td></tr>
<tr><td>Chevrolet</td><td>Equinox</td><td>LT2</td><td>2010</td><td> 39.9 </td><td> 51.3 </td><td> 58.4 </td><td> 62.0 </td><td> 65.5 </td><td> 69.1 </td></tr>
<tr><td>Chevrolet</td><td>HHR</td><td>2.4</td><td>2008</td><td> 46.0 </td><td> 56.6 </td><td> 65.0 </td><td> 67.7 </td><td> 70.8 </td><td> 74.3 </td></tr>
<tr><td>Chevrolet</td><td>Impala</td><td>2.5</td><td>2013</td><td> 39.3 </td><td> 50.6 </td><td> 57.7 </td><td> 61.3 </td><td> 64.7 </td><td> 68.1 </td></tr>
<tr><td>Chevrolet</td><td>Lacetti</td><td>2.0 TCDI</td><td>2008</td><td> 43.0 </td><td> 53.0 </td><td> 60.9 </td><td> 64.7 </td><td> 66.2 </td><td> 68.1 </td></tr>
<tr><td>Chevrolet</td><td>Malibu</td><td>3.6 V6</td><td>2008</td><td> 44.5 </td><td> 55.0 </td><td> 61.6 </td><td> 65.1 </td><td> 67.8 </td><td> 70.5 </td></tr>
<tr><td>Chevrolet</td><td>Malibu</td><td>2.4</td><td>2012</td><td> 36.7 </td><td> 51.7 </td><td> 60.8 </td><td> 66.3 </td><td> 68.0 </td><td> 69.8 </td></tr>
<tr><td>Chevrolet</td><td>Malibu</td><td>1.5</td><td>2016</td><td> 42.7 </td><td> 55.3 </td><td> 62.9 </td><td> 67.6 </td><td> 68.8 </td><td> 70.0 </td></tr>
<tr><td>Chevrolet</td><td>Orlando</td><td>1.8 LTZ</td><td>2011</td><td> 39.1 </td><td> 57.3 </td><td> 61.2 </td><td> 63.7 </td><td> 66.0 </td><td> 70.0 </td></tr>
<tr><td>Chevrolet</td><td>Silverado</td><td>Hybrid</td><td>2009</td><td> 46.3 </td><td> 57.2 </td><td> 63.8 </td><td> 67.7 </td><td> 69.6 </td><td> 71.5 </td></tr>
<tr><td>Chevrolet</td><td>Silverado</td><td>5.3 V8</td><td>2016</td><td> 42.7 </td><td> 54.5 </td><td> 61.7 </td><td> 66.1 </td><td> 67.4 </td><td> 68.8 </td></tr>
<tr><td>Chevrolet</td><td>Sonic</td><td>1.4</td><td>2012</td><td> 44.4 </td><td> 55.8 </td><td> 62.8 </td><td> 66.7 </td><td> 69.2 </td><td> 71.7 </td></tr>
<tr><td>Chevrolet</td><td>SS</td><td>6.2 V8</td><td>2014</td><td> 45.8 </td><td> 55.3 </td><td> 61.3 </td><td> 64.0 </td><td> 67.9 </td><td> 71.8 </td></tr>
<tr><td>Chevrolet</td><td>Suburban</td><td>5.3 V8</td><td>2016</td><td> 41.7 </td><td> 53.8 </td><td> 61.1 </td><td> 65.6 </td><td> 66.8 </td><td> 68.0 </td></tr>
<tr><td>Chevrolet</td><td>Tahoe</td><td>Hybrid</td><td>2008</td><td> 48.0 </td><td> 56.2 </td><td> 61.3 </td><td> 63.8 </td><td> 66.7 </td><td> 69.7 </td></tr>
<tr><td>Chevrolet</td><td>Tahoe</td><td>5.3 V8</td><td>2013</td><td> 46.0 </td><td> 54.7 </td><td> 60.5 </td><td> 62.4 </td><td> 68.5 </td><td> 74.6 </td></tr>
<tr><td>Chevrolet</td><td>Tahoe</td><td>5.3 V8</td><td>2014</td><td> 39.1 </td><td> 49.9 </td><td> 56.5 </td><td> 60.2 </td><td> 62.5 </td><td> 64.8 </td></tr>
<tr><td>Chevrolet</td><td>Traverse</td><td>3.6 V6</td><td>2009</td><td> 42.4 </td><td> 53.6 </td><td> 60.7 </td><td> 64.3 </td><td> 67.7 </td><td> 71.2 </td></tr>
<tr><td>Chevrolet</td><td>Volt</td><td>electric mode</td><td>2011</td><td> 37.1 </td><td> 52.2 </td><td> 61.3 </td><td> 67.3 </td><td> 67.7 </td><td> 68.2 </td></tr>
<tr><td>Chevrolet</td><td>Volt</td><td>petrol mode</td><td>2011</td><td> 48.7 </td><td> 61.1 </td><td> 68.7 </td><td> 73.3 </td><td> 74.6 </td><td> 76.0 </td></tr>
<tr><td>Chevrolet</td><td>Volt</td><td>&nbsp;</td><td>2012</td><td> 43.3 </td><td> 56.7 </td><td> 62.5 </td><td> 64.8 </td><td> 66.7 </td><td> 70.0 </td></tr>
<tr><td>Chrysler</td><td>200</td><td>&nbsp;</td><td>2011</td><td> 44.8 </td><td> 54.5 </td><td> 60.5 </td><td> 63.6 </td><td> 66.6 </td><td> 69.7 </td></tr>
<tr><td>Chrysler</td><td>300</td><td>&nbsp;</td><td>2011</td><td> 40.9 </td><td> 50.9 </td><td> 57.3 </td><td> 60.4 </td><td> 63.7 </td><td> 67.0 </td></tr>
<tr><td>Chrysler</td><td>Grand Voyager</td><td>2.8 CRD</td><td>2008</td><td> 50.7 </td><td> 58.3 </td><td> 63.7 </td><td> 65.7 </td><td> 68.5 </td><td> 71.4 </td></tr>
<tr><td>Chrysler</td><td>Grand Voyager</td><td>3.8 V6</td><td>2008</td><td> 46.2 </td><td> 56.8 </td><td> 65.3 </td><td> 68.1 </td><td> 71.1 </td><td> 74.5 </td></tr>
<tr><td>Chrysler</td><td>Sebring</td><td>3.5 V6</td><td>2008</td><td> 47.3 </td><td> 56.0 </td><td> 61.6 </td><td> 64.0 </td><td> 67.9 </td><td> 71.8 </td></tr>
<tr><td>Chrysler</td><td>Town and Country</td><td>3.6 V6</td><td>2014</td><td> 42.0 </td><td> 53.0 </td><td> 59.8 </td><td> 63.6 </td><td> 66.1 </td><td> 68.6 </td></tr>
<tr><td>Citroen</td><td>Berlingo</td><td>1.6 16V</td><td>2008</td><td> 44.0 </td><td> 62.8 </td><td> 66.1 </td><td> 68.1 </td><td> 70.9 </td><td> 73.6 </td></tr>
<tr><td>Citroen</td><td>C1</td><td>1.0</td><td>2008</td><td> 52.4 </td><td> 66.2 </td><td> 70.7 </td><td> 73.4 </td><td> 78.6 </td><td> 84.5 </td></tr>
<tr><td>Citroen</td><td>C1</td><td>1.0</td><td>2009</td><td> 48.8 </td><td> 65.4 </td><td> 68.4 </td><td> 71.2 </td><td> 75.0 </td><td> 77.4 </td></tr>
<tr><td>Citroen</td><td>C1</td><td>1.0</td><td>2009</td><td> 47.3 </td><td> 58.2 </td><td> 67.0 </td><td> 71.8 </td><td> 72.8 </td><td> 74.2 </td></tr>
<tr><td>Citroen</td><td>C1</td><td>1.0</td><td>2012</td><td> 47.3 </td><td> 58.2 </td><td> 67.0 </td><td> 71.8 </td><td> 72.8 </td><td> 74.2 </td></tr>
<tr><td>Citroen</td><td>C1</td><td>1.0</td><td>2013</td><td> 43.4 </td><td> 61.3 </td><td> 66.7 </td><td> 69.3 </td><td> 74.2 </td><td> 76.1 </td></tr>
<tr><td>Citroen</td><td>C3</td><td>1.4 VTI Picasso</td><td>2009</td><td> 44.1 </td><td> 60.8 </td><td> 63.5 </td><td> 65.8 </td><td> 69.4 </td><td> 71.6 </td></tr>
<tr><td>Citroen</td><td>C3</td><td>1.4 VTI</td><td>2010</td><td> 36.7 </td><td> 59.2 </td><td> 63.2 </td><td> 66.7 </td><td> 68.6 </td><td> 72.4 </td></tr>
<tr><td>Citroen</td><td>C3</td><td>1.6 Picasso</td><td>2013</td><td> 39.7 </td><td> 58.6 </td><td> 64.7 </td><td> 68.0 </td><td> 71.2 </td><td> 74.0 </td></tr>
<tr><td>Citroen</td><td>C3</td><td>1.2</td><td>2017</td><td> 46.2 </td><td> 55.1 </td><td> 61.2 </td><td> 64.1 </td><td> 71.1 </td><td> 71.2 </td></tr>
<tr><td>Citroen</td><td>C3</td><td>1.2 Aircross</td><td>2017</td><td> 38.7 </td><td> 57.2 </td><td> 62.8 </td><td> 64.2 </td><td> 71.3 </td><td> 71.3 </td></tr>
<tr><td>Citroen</td><td>C3</td><td>1.6d</td><td>2017</td><td> 46.9 </td><td> 60.8 </td><td> 64.0 </td><td> 67.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>1.6 16V Coupe</td><td>2008</td><td> 41.4 </td><td> 62.2 </td><td> 65.5 </td><td> 67.7 </td><td> 70.3 </td><td> 72.1 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>1.6 THP</td><td>2008</td><td> 43.7 </td><td> 53.8 </td><td> 61.8 </td><td> 66.4 </td><td> 67.2 </td><td> 68.3 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>2.0 HDiF</td><td>2008</td><td> 40.7 </td><td> 50.1 </td><td> 57.6 </td><td> 61.6 </td><td> 62.6 </td><td> 63.9 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>1.6 VTI</td><td>2009</td><td> 42.6 </td><td> 62.8 </td><td> 64.8 </td><td> 67.9 </td><td> 69.6 </td><td> 72.3 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>1.6 VTI Picasso </td><td>2009</td><td> 40.9 </td><td> 59.8 </td><td> 63.9 </td><td> 66.0 </td><td> 69.7 </td><td> 71.8 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>1.6 VTI</td><td>2010</td><td> 39.2 </td><td> 58.4 </td><td> 63.3 </td><td> 66.3 </td><td> 69.2 </td><td> 71.7 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>1.6 e-HDI</td><td>2011</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 66.7 </td><td> 68.0 </td><td> 69.7 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>1.6 THP Picasso</td><td>2011</td><td> 38.6 </td><td> 39.6 </td><td> 62.1 </td><td> 64.9 </td><td> 68.2 </td><td> 70.6 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>1.6 Aircross</td><td>2012</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 68.3 </td><td> 69.2 </td><td> 70.5 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>1.6 Picasso</td><td>2012</td><td> 45.2 </td><td> 55.6 </td><td> 63.9 </td><td> 67.1 </td><td> 69.6 </td><td> 72.5 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>1.6 Picasso</td><td>2013</td><td> 42.4 </td><td> 55.8 </td><td> 60.7 </td><td> 62.3 </td><td> 65.3 </td><td> 68.1 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>Cactus 1.2</td><td>2014</td><td> 39.6 </td><td> 59.3 </td><td> 63.0 </td><td> 66.5 </td><td> 68.5 </td><td> 72.1 </td></tr>
<tr><td>Citroen</td><td>C4</td><td>2.0 HDi Grand Picasso</td><td>2015</td><td> 42.3 </td><td> 59.2 </td><td> 62.1 </td><td> 64.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Citroen</td><td>C4 Picasso</td><td>1.2 Picasso</td><td>2017</td><td> 40.5 </td><td> 54.9 </td><td> 58.7 </td><td> 62.3 </td><td> 69.0 </td><td> 69.1 </td></tr>
<tr><td>Citroen</td><td>C5</td><td>2.0 HDiF</td><td>2008</td><td> 41.2 </td><td> 50.7 </td><td> 58.3 </td><td> 61.2 </td><td> 63.5 </td><td> 66.0 </td></tr>
<tr><td>Citroen</td><td>C5</td><td>2.0 HDiF Stationcar</td><td>2008</td><td> 43.4 </td><td> 53.4 </td><td> 61.5 </td><td> 64.3 </td><td> 66.9 </td><td> 69.9 </td></tr>
<tr><td>Citroen</td><td>C5</td><td>2.0 Stationcar</td><td>2008</td><td> 39.0 </td><td> 59.3 </td><td> 62.2 </td><td> 64.0 </td><td> 67.1 </td><td> 69.4 </td></tr>
<tr><td>Citroen</td><td>C5</td><td>2.7 V6 HDiF</td><td>2008</td><td> 44.1 </td><td> 63.0 </td><td> 66.0 </td><td> 68.0 </td><td> 70.0 </td><td> 72.0 </td></tr>
<tr><td>Citroen</td><td>C5</td><td>2.0</td><td>2009</td><td> 45.4 </td><td> 55.9 </td><td> 64.3 </td><td> 67.2 </td><td> 70.0 </td><td> 73.2 </td></tr>
<tr><td>Citroen</td><td>C5</td><td>3.0 HDiF</td><td>2010</td><td> 44.1 </td><td> 54.3 </td><td> 62.5 </td><td> 66.7 </td><td> 67.9 </td><td> 69.5 </td></tr>
<tr><td>Citroen</td><td>C5</td><td>1.6 THP Tourer</td><td>2011</td><td> 43.7 </td><td> 53.8 </td><td> 61.8 </td><td> 65.3 </td><td> 67.2 </td><td> 69.5 </td></tr>
<tr><td>Citroen</td><td>C6</td><td>2.7 HDiF</td><td>2008</td><td> 42.9 </td><td> 52.8 </td><td> 60.7 </td><td> 64.0 </td><td> 66.1 </td><td> 68.4 </td></tr>
<tr><td>Citroen</td><td>C6</td><td>3.0</td><td>2008</td><td> 41.1 </td><td> 56.5 </td><td> 60.1 </td><td> 62.2 </td><td> 65.2 </td><td> 67.3 </td></tr>
<tr><td>Citroen</td><td>C-Crosser</td><td>2.2 HDiF</td><td>2008</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 67.6 </td><td> 68.2 </td><td> 69.1 </td></tr>
<tr><td>Citroen</td><td>C-Zero</td><td>&nbsp;</td><td>2011</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 67.5 </td><td> 69.2 </td><td> 71.3 </td></tr>
<tr><td>Citroen</td><td>DS3</td><td>1.6 VTI</td><td>2010</td><td> 38.1 </td><td> 63.1 </td><td> 65.4 </td><td> 67.9 </td><td> 70.6 </td><td> 71.7 </td></tr>
<tr><td>Citroen</td><td>DS4</td><td>1.6</td><td>2011</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 65.6 </td><td> 68.4 </td><td> 71.6 </td></tr>
<tr><td>Citroen</td><td>DS4</td><td>1.6 THP 200</td><td>2011</td><td> 43.6 </td><td> 57.7 </td><td> 61.7 </td><td> 63.9 </td><td> 67.1 </td><td> 69.5 </td></tr>
<tr><td>Citroen</td><td>DS4</td><td>VTi</td><td>2011</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 65.6 </td><td> 68.4 </td><td> 71.6 </td></tr>
<tr><td>Citroen</td><td>DS5</td><td>HDI</td><td>2012</td><td> 48.3 </td><td> 57.4 </td><td> 62.6 </td><td> 63.2 </td><td> 66.1 </td><td> 70.5 </td></tr>
<tr><td>Dacia</td><td>Duster</td><td>1.6</td><td>2010</td><td> 49.2 </td><td> 65.1 </td><td> 68.1 </td><td> 71.1 </td><td> 75.1 </td><td> 78.1 </td></tr>
<tr><td>Dacia</td><td>Duster</td><td>1.6 16v</td><td>2012</td><td> 43.7 </td><td> 61.3 </td><td> 66.6 </td><td> 68.2 </td><td> 71.9 </td><td> 76.4 </td></tr>
<tr><td>Dacia</td><td>Duster</td><td>1.2</td><td>2014</td><td> 41.3 </td><td> 57.7 </td><td> 63.5 </td><td> 66.2 </td><td> 70.4 </td><td> 72.9 </td></tr>
<tr><td>Dacia</td><td>Duster</td><td>1.2</td><td>2015</td><td> 44.2 </td><td> 61.2 </td><td> 64.6 </td><td> 67.9 </td><td> 70.6 </td><td> 72.3 </td></tr>
<tr><td>Dacia</td><td>Lodgy</td><td>1.2</td><td>2013</td><td> 47.6 </td><td> 60.2 </td><td> 65.2 </td><td> 69.9 </td><td> 73.3 </td><td> 75.3 </td></tr>
<tr><td>Dacia</td><td>Logan</td><td>1.4 MPI</td><td>2008</td><td> 46.7 </td><td> 64.2 </td><td> 68.0 </td><td> 70.6 </td><td> 75.2 </td><td> 80.4 </td></tr>
<tr><td>Dacia</td><td>Logan</td><td>1.6</td><td>2008</td><td> 47.0 </td><td> 57.8 </td><td> 66.5 </td><td> 69.8 </td><td> 72.4 </td><td> 75.4 </td></tr>
<tr><td>Dacia</td><td>Logan</td><td>1.6</td><td>2009</td><td> 47.2 </td><td> 58.1 </td><td> 66.8 </td><td> 69.2 </td><td> 72.7 </td><td> 76.7 </td></tr>
<tr><td>Dacia</td><td>Sandero</td><td>1.6</td><td>2008</td><td> 47.1 </td><td> 57.9 </td><td> 66.6 </td><td> 70.2 </td><td> 72.5 </td><td> 75.0 </td></tr>
<tr><td>Dacia</td><td>Sandero</td><td>1.2 16V</td><td>2010</td><td> 42.7 </td><td> 64.5 </td><td> 67.3 </td><td> 70.9 </td><td> 73.4 </td><td> 76.8 </td></tr>
<tr><td>Dacia</td><td>Sandero</td><td>0.9</td><td>2013</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 65.9 </td><td> 67.5 </td><td> 69.5 </td></tr>
<tr><td>Daihatsu</td><td>Cuore</td><td>1.0</td><td>2009</td><td> 47.2 </td><td> 58.1 </td><td> 66.8 </td><td> 70.1 </td><td> 72.7 </td><td> 75.7 </td></tr>
<tr><td>Daihatsu</td><td>Materia</td><td>1.3</td><td>2008</td><td> 45.7 </td><td> 56.2 </td><td> 64.7 </td><td> 67.9 </td><td> 70.4 </td><td> 73.3 </td></tr>
<tr><td>Daihatsu</td><td>Sirion</td><td>1.0</td><td>2008</td><td> 46.4 </td><td> 57.1 </td><td> 65.7 </td><td> 69.1 </td><td> 71.5 </td><td> 74.1 </td></tr>
<tr><td>Daihatsu</td><td>Sirion2</td><td>1.0</td><td>2008</td><td> 46.7 </td><td> 64.0 </td><td> 69.7 </td><td> 72.5 </td><td> 75.9 </td><td> 79.8 </td></tr>
<tr><td>Dodge</td><td>Avenger</td><td>2.0</td><td>2008</td><td> 44.7 </td><td> 55.0 </td><td> 63.3 </td><td> 67.6 </td><td> 68.8 </td><td> 70.4 </td></tr>
<tr><td>Dodge</td><td>Caliber</td><td>2.4</td><td>2008</td><td> 46.0 </td><td> 56.6 </td><td> 65.0 </td><td> 68.1 </td><td> 70.8 </td><td> 73.9 </td></tr>
<tr><td>Dodge</td><td>Caliber</td><td>SRT-4</td><td>2008</td><td> 52.8 </td><td> 59.9 </td><td> 64.4 </td><td> 66.3 </td><td> 69.8 </td><td> 73.4 </td></tr>
<tr><td>Dodge</td><td>Challenger</td><td>SRT8</td><td>2008</td><td> 48.8 </td><td> 59.7 </td><td> 66.5 </td><td> 69.9 </td><td> 73.4 </td><td> 76.9 </td></tr>
<tr><td>Dodge</td><td>Challenger</td><td>SRT8</td><td>2011</td><td> 51.2 </td><td> 59.3 </td><td> 64.5 </td><td> 66.7 </td><td> 70.6 </td><td> 74.5 </td></tr>
<tr><td>Dodge</td><td>Challenger</td><td>5.7 V8</td><td>2016</td><td> 45.3 </td><td> 57.5 </td><td> 65.1 </td><td> 69.2 </td><td> 72.2 </td><td> 75.2 </td></tr>
<tr><td>Dodge</td><td>Charger</td><td>SRT8</td><td>2012</td><td> 46.4 </td><td> 55.9 </td><td> 62.0 </td><td> 64.7 </td><td> 68.8 </td><td> 72.9 </td></tr>
<tr><td>Dodge</td><td>Dart</td><td>1.4 turbo</td><td>2012</td><td> 42.3 </td><td> 52.8 </td><td> 59.4 </td><td> 62.9 </td><td> 65.6 </td><td> 68.3 </td></tr>
<tr><td>Dodge</td><td>Journey</td><td>2.4</td><td>2008</td><td> 43.2 </td><td> 53.2 </td><td> 61.2 </td><td> 64.8 </td><td> 66.5 </td><td> 68.6 </td></tr>
<tr><td>Dodge</td><td>Journey</td><td>3.6 V6</td><td>2016</td><td> 43.1 </td><td> 55.5 </td><td> 63.0 </td><td> 67.8 </td><td> 68.4 </td><td> 69.0 </td></tr>
<tr><td>Dodge</td><td>Ram</td><td>1500</td><td>2009</td><td> 43.5 </td><td> 54.7 </td><td> 61.6 </td><td> 65.3 </td><td> 67.9 </td><td> 70.6 </td></tr>
<tr><td>Dodge</td><td>Ram</td><td>5.7 V8</td><td>2010</td><td> 39.2 </td><td> 47.5 </td><td> 52.6 </td><td> 55.3 </td><td> 57.8 </td><td> 60.3 </td></tr>
<tr><td>Dodge</td><td>Ram</td><td>3.6 V6</td><td>2012</td><td> 40.1 </td><td> 51.0 </td><td> 57.9 </td><td> 61.3 </td><td> 64.9 </td><td> 68.4 </td></tr>
<tr><td>Dodge</td><td>Ram</td><td>1500 3.6 V6</td><td>2013</td><td> 39.2 </td><td> 51.6 </td><td> 59.4 </td><td> 63.4 </td><td> 67.1 </td><td> 70.8 </td></tr>
<tr><td>Dodge</td><td>Viper</td><td>SRT-10</td><td>2008</td><td> 61.3 </td><td> 68.6 </td><td> 73.3 </td><td> 75.0 </td><td> 79.4 </td><td> 83.8 </td></tr>
<tr><td>Dodge</td><td>Viper</td><td>8.4 V10</td><td>2013</td><td> 60.1 </td><td> 67.5 </td><td> 72.3 </td><td> 74.1 </td><td> 78.4 </td><td> 82.7 </td></tr>
<tr><td>DS</td><td>4</td><td>1.6D</td><td>2016</td><td> 42.6 </td><td> 54.8 </td><td> 60.8 </td><td> 61.8 </td><td> 66.4 </td><td> 69.4 </td></tr>
<tr><td>DS</td><td>5</td><td>&nbsp;</td><td>2015</td><td> 40.2 </td><td> 58.3 </td><td> 61.8 </td><td> 64.3 </td><td> 68.1 </td><td> 70.1 </td></tr>
<tr><td>Fiat</td><td>124</td><td>1.4</td><td>2016</td><td> 47.9 </td><td> 64.7 </td><td> 69.0 </td><td> 73.3 </td><td> 76.0 </td><td> 79.9 </td></tr>
<tr><td>Fiat</td><td>500</td><td>1.4</td><td>2008</td><td> 46.5 </td><td> 57.2 </td><td> 65.8 </td><td> 70.2 </td><td> 71.5 </td><td> 73.2 </td></tr>
<tr><td>Fiat</td><td>500</td><td>1.2</td><td>2009</td><td> 46.8 </td><td> 57.6 </td><td> 66.2 </td><td> 70.5 </td><td> 72.0 </td><td> 73.9 </td></tr>
<tr><td>Fiat</td><td>500</td><td>0.9 TwinAir Plus</td><td>2011</td><td> 47.1 </td><td> 59.6 </td><td> 64.5 </td><td> 67.7 </td><td> 72.6 </td><td> 76.6 </td></tr>
<tr><td>Fiat</td><td>500</td><td>1.4</td><td>2011</td><td> 47.7 </td><td> 57.5 </td><td> 63.5 </td><td> 66.7 </td><td> 69.3 </td><td> 72.0 </td></tr>
<tr><td>Fiat</td><td>500</td><td>&nbsp;</td><td>2012</td><td> 45.0 </td><td> 56.4 </td><td> 63.5 </td><td> 67.3 </td><td> 70.1 </td><td> 72.9 </td></tr>
<tr><td>Fiat</td><td>500</td><td>Abarth</td><td>2012</td><td> 49.0 </td><td> 59.9 </td><td> 66.7 </td><td> 70.2 </td><td> 73.1 </td><td> 76.0 </td></tr>
<tr><td>Fiat</td><td>500</td><td>&nbsp;</td><td>2015</td><td> 47.8 </td><td> 59.4 </td><td> 65.1 </td><td> 68.0 </td><td> 73.7 </td><td> 76.1 </td></tr>
<tr><td>Fiat</td><td>500 C</td><td>0.9</td><td>2013</td><td> 45.9 </td><td> 61.5 </td><td> 65.0 </td><td> 68.4 </td><td> 72.2 </td><td> 76.5 </td></tr>
<tr><td>Fiat</td><td>500 L</td><td>0.9</td><td>2013</td><td> 42.4 </td><td> 61.5 </td><td> 65.5 </td><td> 66.7 </td><td> 71.1 </td><td> 73.9 </td></tr>
<tr><td>Fiat</td><td>500 L</td><td>1.3</td><td>2013</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 68.0 </td><td> 68.7 </td><td> 69.8 </td></tr>
<tr><td>Fiat</td><td>500X</td><td>1.4</td><td>2015</td><td> 39.9 </td><td> 57.6 </td><td> 62.4 </td><td> 65.9 </td><td> 69.4 </td><td> 72.9 </td></tr>
<tr><td>Fiat</td><td>Bravo</td><td>1.4</td><td>2008</td><td> 44.6 </td><td> 54.9 </td><td> 63.1 </td><td> 67.3 </td><td> 68.6 </td><td> 70.3 </td></tr>
<tr><td>Fiat</td><td>Bravo</td><td>2.0 MultiJet</td><td>2009</td><td> 46.8 </td><td> 61.4 </td><td> 65.4 </td><td> 67.6 </td><td> 70.4 </td><td> 72.1 </td></tr>
<tr><td>Fiat</td><td>Doblo</td><td>1.4</td><td>2011</td><td> 45.9 </td><td> 56.5 </td><td> 65.0 </td><td> 68.3 </td><td> 70.7 </td><td> 73.3 </td></tr>
<tr><td>Fiat</td><td>Grande Punto</td><td>1.3 MultiJet 16v</td><td>2011</td><td> 43.4 </td><td> 60.5 </td><td> 64.1 </td><td> 67.2 </td><td> 69.8 </td><td> 74.6 </td></tr>
<tr><td>Fiat</td><td>Panda</td><td>1.2</td><td>2008</td><td> 48.3 </td><td> 63.9 </td><td> 70.2 </td><td> 71.7 </td><td> 75.1 </td><td> 79.0 </td></tr>
<tr><td>Fiat</td><td>Panda</td><td>0.9</td><td>2012</td><td> 46.7 </td><td> 57.5 </td><td> 66.1 </td><td> 69.4 </td><td> 72.0 </td><td> 75.0 </td></tr>
<tr><td>Fiat</td><td>Panda</td><td>0.9</td><td>2013</td><td> 44.8 </td><td> 58.1 </td><td> 65.5 </td><td> 68.9 </td><td> 72.4 </td><td> 76.1 </td></tr>
<tr><td>Fiat</td><td>Punto</td><td>0.9</td><td>2012</td><td> 43.7 </td><td> 53.8 </td><td> 61.9 </td><td> 66.2 </td><td> 67.3 </td><td> 68.8 </td></tr>
<tr><td>Fiat</td><td>Punto Evo</td><td>1.3D</td><td>2010</td><td> 44.1 </td><td> 54.3 </td><td> 62.5 </td><td> 65.7 </td><td> 68.0 </td><td> 70.5 </td></tr>
<tr><td>Fiat</td><td>Punto Evo</td><td>1.4</td><td>2010</td><td> 45.6 </td><td> 56.1 </td><td> 64.5 </td><td> 67.3 </td><td> 70.2 </td><td> 73.5 </td></tr>
<tr><td>Fiat</td><td>Punto Evo</td><td>1.4 MultiAir</td><td>2010</td><td> 39.3 </td><td> 60.5 </td><td> 64.6 </td><td> 67.2 </td><td> 71.0 </td><td> 73.5 </td></tr>
<tr><td>Fiat</td><td>Punto Evo</td><td>1.3 MultiJet 16v</td><td>2011</td><td> 45.4 </td><td> 59.5 </td><td> 64.8 </td><td> 66.1 </td><td> 68.8 </td><td> 69.4 </td></tr>
<tr><td>Fiat</td><td>Qubo</td><td>1.4</td><td>2009</td><td> 46.3 </td><td> 57.0 </td><td> 65.5 </td><td> 68.5 </td><td> 71.3 </td><td> 74.5 </td></tr>
<tr><td>Fiat</td><td>Sedici</td><td>1.6</td><td>2008</td><td> 45.6 </td><td> 56.1 </td><td> 64.5 </td><td> 67.9 </td><td> 70.2 </td><td> 72.7 </td></tr>
<tr><td>Fiat</td><td>Sedici</td><td>1.6</td><td>2010</td><td> 45.4 </td><td> 55.8 </td><td> 64.2 </td><td> 66.6 </td><td> 69.9 </td><td> 73.6 </td></tr>
<tr><td>Fiat</td><td>Tipo</td><td>1.6d</td><td>2017</td><td> 46.8 </td><td> 56.3 </td><td> 61.1 </td><td> 64.1 </td><td> 70.6 </td><td> 70.7 </td></tr>
<tr><td>Ford</td><td>B-Max</td><td>1.0</td><td>2012</td><td> 44.9 </td><td> 57.4 </td><td> 61.8 </td><td> 66.7 </td><td> 69.2 </td><td> 71.9 </td></tr>
<tr><td>Ford</td><td>C-Max</td><td>1.6 Ecoboost</td><td>2011</td><td> 44.5 </td><td> 59.5 </td><td> 62.5 </td><td> 66.0 </td><td> 68.5 </td><td> 71.0 </td></tr>
<tr><td>Ford</td><td>C-Max</td><td>1.6 TDCI</td><td>2011</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 64.4 </td><td> 68.4 </td><td> 72.9 </td></tr>
<tr><td>Ford</td><td>C-Max</td><td>2.0 TDCI</td><td>2011</td><td> 44.6 </td><td> 54.9 </td><td> 63.1 </td><td> 66.7 </td><td> 68.6 </td><td> 70.9 </td></tr>
<tr><td>Ford</td><td>C-Max</td><td>Hybrid</td><td>2012</td><td> 39.5 </td><td> 51.5 </td><td> 59.1 </td><td> 63.0 </td><td> 66.4 </td><td> 69.8 </td></tr>
<tr><td>Ford</td><td>C-Max</td><td>1.6</td><td>2014</td><td> 44.5 </td><td> 58.4 </td><td> 61.7 </td><td> 64.9 </td><td> 68.5 </td><td> 70.9 </td></tr>
<tr><td>Ford</td><td>C-Max</td><td>1.0</td><td>2016</td><td> 38.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Ford</td><td>EcoSport</td><td>1.0</td><td>2014</td><td> 48.8 </td><td> 69.1 </td><td> 70.0 </td><td> 73.1 </td><td> 75.0 </td><td> 79.8 </td></tr>
<tr><td>Ford</td><td>EcoSport</td><td>1.0</td><td>2014</td><td> 42.9 </td><td> 57.0 </td><td> 60.5 </td><td> 65.7 </td><td> 68.7 </td><td> 71.7 </td></tr>
<tr><td>Ford</td><td>Edge</td><td>&nbsp;</td><td>2011</td><td> 39.2 </td><td> 54.8 </td><td> 64.6 </td><td> 69.6 </td><td> 74.1 </td><td> 78.6 </td></tr>
<tr><td>Ford</td><td>Edge</td><td>2.0D</td><td>2016</td><td> 41.5 </td><td> 53.7 </td><td> 58.3 </td><td> 62.7 </td><td> 66.2 </td><td> 68.3 </td></tr>
<tr><td>Ford</td><td>Escape</td><td>3.0 V6</td><td>2008</td><td> 45.1 </td><td> 56.8 </td><td> 63.9 </td><td> 68.1 </td><td> 69.9 </td><td> 71.7 </td></tr>
<tr><td>Ford</td><td>Expedition</td><td>5.4 V8</td><td>2008</td><td> 44.1 </td><td> 56.3 </td><td> 63.6 </td><td> 68.2 </td><td> 69.1 </td><td> 70.0 </td></tr>
<tr><td>Ford</td><td>Explorer</td><td>3.5 V6</td><td>2011</td><td> 40.9 </td><td> 52.8 </td><td> 60.1 </td><td> 64.2 </td><td> 66.6 </td><td> 69.1 </td></tr>
<tr><td>Ford</td><td>F-150</td><td>5.4 V8</td><td>2009</td><td> 47.6 </td><td> 56.5 </td><td> 62.1 </td><td> 64.9 </td><td> 67.6 </td><td> 70.4 </td></tr>
<tr><td>Ford</td><td>F-150</td><td>SVT Raptor</td><td>2010</td><td> 37.5 </td><td> 48.6 </td><td> 55.5 </td><td> 59.1 </td><td> 62.4 </td><td> 65.8 </td></tr>
<tr><td>Ford</td><td>F-150</td><td>&nbsp;</td><td>2011</td><td> 45.2 </td><td> 54.3 </td><td> 60.0 </td><td> 62.7 </td><td> 65.9 </td><td> 69.1 </td></tr>
<tr><td>Ford</td><td>F-150</td><td>3.7 V6</td><td>2013</td><td> 41.6 </td><td> 53.1 </td><td> 60.3 </td><td> 64.0 </td><td> 67.4 </td><td> 70.8 </td></tr>
<tr><td>Ford</td><td>F-150</td><td>3.5 V6</td><td>2016</td><td> 43.4 </td><td> 54.0 </td><td> 60.6 </td><td> 64.2 </td><td> 66.6 </td><td> 69.0 </td></tr>
<tr><td>Ford</td><td>F-450</td><td>6.4 V8</td><td>2008</td><td> 51.4 </td><td> 59.7 </td><td> 64.6 </td><td> 67.9 </td><td> 68.0 </td><td> 68.2 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>1.4</td><td>2008</td><td> 45.4 </td><td> 55.8 </td><td> 64.2 </td><td> 67.4 </td><td> 69.9 </td><td> 72.6 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>1.6 TDCI</td><td>2008</td><td> 46.3 </td><td> 62.7 </td><td> 65.8 </td><td> 68.9 </td><td> 71.7 </td><td> 75.7 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>1.25</td><td>2009</td><td> 41.5 </td><td> 61.4 </td><td> 66.1 </td><td> 68.0 </td><td> 71.2 </td><td> 73.4 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>1.6 </td><td>2009</td><td> 40.3 </td><td> 55.4 </td><td> 64.6 </td><td> 70.1 </td><td> 72.3 </td><td> 74.5 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>1.25</td><td>2010</td><td> 39.6 </td><td> 61.6 </td><td> 65.3 </td><td> 67.5 </td><td> 70.3 </td><td> 71.9 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>1.6</td><td>2011</td><td> 44.2 </td><td> 55.0 </td><td> 61.6 </td><td> 65.3 </td><td> 67.7 </td><td> 70.1 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>1.0</td><td>2013</td><td> 43.7 </td><td> 57.1 </td><td> 61.9 </td><td> 64.9 </td><td> 67.4 </td><td> 71.0 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>ST</td><td>2013</td><td> 48.1 </td><td> 59.7 </td><td> 64.7 </td><td> 65.4 </td><td> 68.3 </td><td> 72.4 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>1.6</td><td>2014</td><td> 45.2 </td><td> 55.2 </td><td> 61.4 </td><td> 64.6 </td><td> 67.5 </td><td> 70.4 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>1.0</td><td>2016</td><td> 39.1 </td><td> 59.2 </td><td> 62.8 </td><td> 66.3 </td><td> 68.3 </td><td> 71.8 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>ST</td><td>2016</td><td> 45.9 </td><td> 62.7 </td><td> 65.0 </td><td> 67.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Ford</td><td>Fiesta</td><td>1.0</td><td>2017</td><td> 40.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Ford</td><td>Flex</td><td>3.5 V6</td><td>2009</td><td> 44.6 </td><td> 55.3 </td><td> 62.0 </td><td> 65.6 </td><td> 68.0 </td><td> 70.4 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.6 TDCI</td><td>2008</td><td> 45.8 </td><td> 56.3 </td><td> 64.8 </td><td> 67.6 </td><td> 70.5 </td><td> 73.8 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>2.0</td><td>2008</td><td> 46.7 </td><td> 57.4 </td><td> 66.1 </td><td> 69.3 </td><td> 71.9 </td><td> 74.9 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>2.0 Coupe-Cabrio</td><td>2008</td><td> 46.6 </td><td> 57.4 </td><td> 66.0 </td><td> 69.3 </td><td> 71.8 </td><td> 74.7 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>Econetic</td><td>2008</td><td> 45.9 </td><td> 63.4 </td><td> 65.2 </td><td> 68.5 </td><td> 70.3 </td><td> 72.9 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>ST</td><td>2008</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 67.0 </td><td> 69.1 </td><td> 71.4 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.8</td><td>2009</td><td> 43.7 </td><td> 57.9 </td><td> 62.8 </td><td> 65.3 </td><td> 66.5 </td><td> 69.2 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>RS</td><td>2009</td><td> 44.9 </td><td> 55.3 </td><td> 63.6 </td><td> 67.2 </td><td> 69.1 </td><td> 71.4 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>ST</td><td>2009</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 67.0 </td><td> 69.1 </td><td> 71.4 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.6 Coupe Cabrio</td><td>2010</td><td> 43.3 </td><td> 61.4 </td><td> 63.9 </td><td> 66.6 </td><td> 69.7 </td><td> 71.6 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.8</td><td>2010</td><td> 46.5 </td><td> 57.3 </td><td> 65.9 </td><td> 68.2 </td><td> 71.7 </td><td> 75.7 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.6</td><td>2011</td><td> 44.0 </td><td> 55.1 </td><td> 61.6 </td><td> 63.6 </td><td> 67.8 </td><td> 71.6 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.6</td><td>2011</td><td> 39.0 </td><td> 55.4 </td><td> 61.1 </td><td> 64.2 </td><td> 66.9 </td><td> 70.8 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.6 TDCI</td><td>2011</td><td> 45.2 </td><td> 55.6 </td><td> 63.9 </td><td> 68.4 </td><td> 69.5 </td><td> 71.0 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.0</td><td>2012</td><td> 38.4 </td><td> 56.4 </td><td> 61.5 </td><td> 64.3 </td><td> 66.7 </td><td> 69.8 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.6 Stationcar</td><td>2012</td><td> 43.5 </td><td> 53.5 </td><td> 61.5 </td><td> 65.2 </td><td> 66.9 </td><td> 69.0 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.6 TDCI</td><td>2012</td><td> 42.6 </td><td> 59.4 </td><td> 62.7 </td><td> 65.7 </td><td> 68.5 </td><td> 70.6 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>ST</td><td>2012</td><td> 46.3 </td><td> 55.2 </td><td> 60.9 </td><td> 63.3 </td><td> 67.4 </td><td> 71.6 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.0</td><td>2013</td><td> 44.5 </td><td> 54.7 </td><td> 62.9 </td><td> 65.8 </td><td> 68.5 </td><td> 71.6 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.0 Stationcar</td><td>2013</td><td> 38.5 </td><td> 55.6 </td><td> 60.6 </td><td> 64.2 </td><td> 68.2 </td><td> 71.5 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.0</td><td>2014</td><td> 39.3 </td><td> 58.2 </td><td> 64.3 </td><td> 67.8 </td><td> 69.8 </td><td> 71.9 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.0</td><td>2015</td><td> 39.3 </td><td> 56.3 </td><td> 62.3 </td><td> 64.9 </td><td> 68.4 </td><td> 71.8 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.0</td><td>2016</td><td> 38.9 </td><td> 58.8 </td><td> 62.5 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>2.0D</td><td>2016</td><td> 49.9 </td><td> 58.8 </td><td> 62.5 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>RS</td><td>2016</td><td> 49.9 </td><td> 61.8 </td><td> 64.0 </td><td> 66.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>ST</td><td>2016</td><td> 45.9 </td><td> 59.6 </td><td> 62.2 </td><td> 65.5 </td><td> 68.8 </td><td> 70.6 </td></tr>
<tr><td>Ford</td><td>Focus</td><td>1.0</td><td>2017</td><td> 36.9 </td><td> 57.8 </td><td> 62.0 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Ford</td><td>Fusion</td><td>Hybrid</td><td>2010</td><td> 41.2 </td><td> 52.6 </td><td> 59.7 </td><td> 63.7 </td><td> 65.8 </td><td> 68.0 </td></tr>
<tr><td>Ford</td><td>Fusion</td><td>2.0</td><td>2012</td><td> 43.2 </td><td> 53.2 </td><td> 59.4 </td><td> 62.7 </td><td> 65.1 </td><td> 67.5 </td></tr>
<tr><td>Ford</td><td>Fusion</td><td>Hybrid</td><td>2012</td><td> 36.7 </td><td> 49.1 </td><td> 57.1 </td><td> 60.6 </td><td> 66.1 </td><td> 71.6 </td></tr>
<tr><td>Ford</td><td>Fusion</td><td>Hybrid</td><td>2013</td><td> 35.6 </td><td> 49.4 </td><td> 58.1 </td><td> 62.2 </td><td> 67.3 </td><td> 72.3 </td></tr>
<tr><td>Ford</td><td>Galaxy</td><td>2.3</td><td>2008</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 65.9 </td><td> 68.3 </td><td> 70.9 </td></tr>
<tr><td>Ford</td><td>Grand C-Max</td><td>1.6</td><td>2012</td><td> 44.5 </td><td> 56.1 </td><td> 62.3 </td><td> 65.6 </td><td> 68.6 </td><td> 72.4 </td></tr>
<tr><td>Ford</td><td>Ka</td><td>1.3</td><td>2008</td><td> 50.2 </td><td> 64.1 </td><td> 68.1 </td><td> 70.6 </td><td> 75.6 </td><td> 81.3 </td></tr>
<tr><td>Ford</td><td>Ka</td><td>1.2</td><td>2009</td><td> 45.8 </td><td> 56.4 </td><td> 64.9 </td><td> 68.5 </td><td> 70.6 </td><td> 72.9 </td></tr>
<tr><td>Ford</td><td>Ka</td><td>1.2</td><td>2013</td><td> 44.0 </td><td> 61.3 </td><td> 66.3 </td><td> 68.1 </td><td> 71.9 </td><td> 74.5 </td></tr>
<tr><td>Ford</td><td>Ka</td><td>1.2</td><td>2017</td><td> 40.9 </td><td> 60.8 </td><td> 64.0 </td><td> 67.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Ford</td><td>Kuga</td><td>2.0 TDCI</td><td>2008</td><td> 45.2 </td><td> 61.9 </td><td> 65.1 </td><td> 68.6 </td><td> 70.3 </td><td> 73.5 </td></tr>
<tr><td>Ford</td><td>Kuga</td><td>2.0 TDCI</td><td>2010</td><td> 45.0 </td><td> 61.1 </td><td> 63.0 </td><td> 66.5 </td><td> 69.2 </td><td> 71.6 </td></tr>
<tr><td>Ford</td><td>Kuga</td><td>1.6</td><td>2013</td><td> 39.7 </td><td> 52.9 </td><td> 58.4 </td><td> 62.0 </td><td> 65.5 </td><td> 68.1 </td></tr>
<tr><td>Ford</td><td>Kuga</td><td>1.5</td><td>2015</td><td> 40.2 </td><td> 54.5 </td><td> 59.8 </td><td> 63.4 </td><td> 67.0 </td><td> 69.4 </td></tr>
<tr><td>Ford</td><td>Mondeo</td><td>2.0 16V Stationcar</td><td>2008</td><td> 44.1 </td><td> 59.5 </td><td> 63.0 </td><td> 67.7 </td><td> 70.3 </td><td> 72.3 </td></tr>
<tr><td>Ford</td><td>Mondeo</td><td>2.3</td><td>2008</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 66.1 </td><td> 67.5 </td><td> 69.3 </td></tr>
<tr><td>Ford</td><td>Mondeo</td><td>2.5T</td><td>2009</td><td> 43.1 </td><td> 62.0 </td><td> 65.0 </td><td> 68.2 </td><td> 71.7 </td><td> 74.0 </td></tr>
<tr><td>Ford</td><td>Mondeo</td><td>1.6 TDCI Stationcar</td><td>2011</td><td> 46.6 </td><td> 58.2 </td><td> 62.1 </td><td> 65.0 </td><td> 68.1 </td><td> 72.3 </td></tr>
<tr><td>Ford</td><td>Mondeo</td><td>2.2 TDCI</td><td>2011</td><td> 43.5 </td><td> 53.5 </td><td> 61.5 </td><td> 64.5 </td><td> 67.0 </td><td> 69.7 </td></tr>
<tr><td>Ford</td><td>Mondeo</td><td>1.6 TDCI</td><td>2012</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 65.6 </td><td> 68.4 </td><td> 71.6 </td></tr>
<tr><td>Ford</td><td>Mondeo</td><td>1.6</td><td>2014</td><td> 36.9 </td><td> 54.8 </td><td> 59.0 </td><td> 63.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Ford</td><td>Mondeo</td><td>2.0D Stationcar</td><td>2015</td><td> 43.8 </td><td> 57.1 </td><td> 61.4 </td><td> 63.1 </td><td> 66.7 </td><td> 69.3 </td></tr>
<tr><td>Ford</td><td>Mondeo</td><td>1.5</td><td>2017</td><td> 44.5 </td><td> 53.6 </td><td> 58.5 </td><td> 62.6 </td><td> 68.5 </td><td> 68.6 </td></tr>
<tr><td>Ford</td><td>Mondeo</td><td>2.0d</td><td>2017</td><td> 43.9 </td><td> 58.8 </td><td> 62.0 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Ford</td><td>Mustang</td><td>Bullit</td><td>2008</td><td> 51.3 </td><td> 60.5 </td><td> 66.4 </td><td> 69.1 </td><td> 72.7 </td><td> 76.3 </td></tr>
<tr><td>Ford</td><td>Mustang</td><td>GT 500</td><td>2008</td><td> 50.4 </td><td> 61.3 </td><td> 68.2 </td><td> 71.6 </td><td> 75.2 </td><td> 78.9 </td></tr>
<tr><td>Ford</td><td>Mustang</td><td>3.7 V6</td><td>2011</td><td> 45.5 </td><td> 58.4 </td><td> 66.4 </td><td> 70.7 </td><td> 73.9 </td><td> 77.1 </td></tr>
<tr><td>Ford</td><td>Mustang</td><td>GT 5.0 V8</td><td>2011</td><td> 48.6 </td><td> 58.5 </td><td> 64.8 </td><td> 67.7 </td><td> 71.7 </td><td> 75.8 </td></tr>
<tr><td>Ford</td><td>Mustang</td><td>Shelby GT500</td><td>2011</td><td> 50.5 </td><td> 62.0 </td><td> 69.2 </td><td> 73.1 </td><td> 75.8 </td><td> 78.5 </td></tr>
<tr><td>Ford</td><td>Mustang</td><td>3.7 V6</td><td>2013</td><td> 45.2 </td><td> 55.7 </td><td> 62.4 </td><td> 65.6 </td><td> 69.5 </td><td> 73.5 </td></tr>
<tr><td>Ford</td><td>Mustang</td><td>5.0 V8</td><td>2016</td><td> 52.8 </td><td> 62.7 </td><td> 66.0 </td><td> 69.3 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>Ford</td><td>Shelby</td><td>GT500</td><td>2014</td><td> 57.3 </td><td> 63.0 </td><td> 66.8 </td><td> 68.0 </td><td> 72.0 </td><td> 76.1 </td></tr>
<tr><td>Ford</td><td>S-Max</td><td>2.2 TDCI</td><td>2008</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 66.5 </td><td> 68.2 </td><td> 70.3 </td></tr>
<tr><td>Ford</td><td>S-Max</td><td>2.0 TDCI</td><td>2010</td><td> 42.4 </td><td> 52.2 </td><td> 60.1 </td><td> 63.8 </td><td> 65.3 </td><td> 67.2 </td></tr>
<tr><td>Ford</td><td>S-Max</td><td>2.0</td><td>2015</td><td> 39.3 </td><td> 54.6 </td><td> 60.1 </td><td> 63.0 </td><td> 65.6 </td><td> 70.2 </td></tr>
<tr><td>Ford</td><td>S-Max</td><td>2.0D</td><td>2016</td><td> 43.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Ford</td><td>Taurus</td><td>3.5 V6</td><td>2010</td><td> 43.5 </td><td> 55.7 </td><td> 63.1 </td><td> 67.6 </td><td> 68.8 </td><td> 70.1 </td></tr>
<tr><td>Ford</td><td>Taurus</td><td>3.5 V6</td><td>2016</td><td> 42.7 </td><td> 55.0 </td><td> 62.5 </td><td> 67.1 </td><td> 68.3 </td><td> 69.5 </td></tr>
<tr><td>Ford </td><td>Ka</td><td>1.2</td><td>2009</td><td> 46.5 </td><td> 64.8 </td><td> 68.9 </td><td> 71.0 </td><td> 75.0 </td><td> 77.4 </td></tr>
<tr><td>Ford </td><td>Mustang</td><td>Shelby GT500</td><td>2013</td><td> 57.3 </td><td> 63.0 </td><td> 66.8 </td><td> 68.0 </td><td> 72.0 </td><td> 76.1 </td></tr>
<tr><td>Genesis</td><td>G80</td><td>3.8 V6</td><td>2016</td><td> 41.2 </td><td> 53.8 </td><td> 61.4 </td><td> 66.1 </td><td> 67.4 </td><td> 68.8 </td></tr>
<tr><td>GMC</td><td>Sierra</td><td>5.3 V8</td><td>2013</td><td> 41.3 </td><td> 51.2 </td><td> 57.4 </td><td> 60.7 </td><td> 63.1 </td><td> 65.5 </td></tr>
<tr><td>GMC</td><td>Sierra</td><td>4.6 V6</td><td>2016</td><td> 43.0 </td><td> 52.3 </td><td> 58.1 </td><td> 61.2 </td><td> 63.6 </td><td> 66.0 </td></tr>
<tr><td>GMC</td><td>Terrain</td><td>3.0 V6</td><td>2010</td><td> 35.6 </td><td> 48.4 </td><td> 56.4 </td><td> 60.8 </td><td> 63.5 </td><td> 66.3 </td></tr>
<tr><td>GMC</td><td>Yukon</td><td>6.2 V8</td><td>2016</td><td> 42.7 </td><td> 54.3 </td><td> 61.3 </td><td> 65.6 </td><td> 66.9 </td><td> 68.3 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>2.0</td><td>2008</td><td> 42.9 </td><td> 52.8 </td><td> 60.7 </td><td> 64.8 </td><td> 66.0 </td><td> 67.6 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>2.2 I-DTEC</td><td>2008</td><td> 50.2 </td><td> 62.1 </td><td> 65.0 </td><td> 66.1 </td><td> 69.5 </td><td> 71.2 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>3.5 V6</td><td>2008</td><td> 40.1 </td><td> 53.4 </td><td> 61.6 </td><td> 66.5 </td><td> 68.1 </td><td> 69.7 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>2.2 I-DTEC Stationcar</td><td>2009</td><td> 45.6 </td><td> 59.5 </td><td> 64.3 </td><td> 66.7 </td><td> 68.4 </td><td> 71.3 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>2.4 Stationcar</td><td>2009</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 64.6 </td><td> 67.2 </td><td> 70.2 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>Crosstour</td><td>2010</td><td> 42.3 </td><td> 51.7 </td><td> 57.6 </td><td> 60.7 </td><td> 63.1 </td><td> 65.5 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>2.4</td><td>2011</td><td> 44.8 </td><td> 53.7 </td><td> 59.3 </td><td> 62.3 </td><td> 64.4 </td><td> 66.6 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>2.0</td><td>2012</td><td> 43.7 </td><td> 53.8 </td><td> 61.8 </td><td> 65.4 </td><td> 67.2 </td><td> 69.4 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>2.4</td><td>2012</td><td> 40.6 </td><td> 51.1 </td><td> 57.6 </td><td> 61.2 </td><td> 63.6 </td><td> 66.1 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>3.5 V6</td><td>2012</td><td> 47.8 </td><td> 57.7 </td><td> 63.9 </td><td> 67.2 </td><td> 69.5 </td><td> 71.9 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>3.5V6</td><td>2012</td><td> 39.7 </td><td> 50.5 </td><td> 57.3 </td><td> 60.7 </td><td> 64.4 </td><td> 68.2 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>2.0 Stationcar</td><td>2013</td><td> 42.4 </td><td> 55.5 </td><td> 61.9 </td><td> 64.3 </td><td> 66.3 </td><td> 70.5 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>2.4</td><td>2013</td><td> 41.0 </td><td> 52.2 </td><td> 59.2 </td><td> 62.9 </td><td> 65.5 </td><td> 68.1 </td></tr>
<tr><td>Honda</td><td>Accord</td><td>Hybrid</td><td>2014</td><td> 35.0 </td><td> 49.6 </td><td> 58.4 </td><td> 63.8 </td><td> 65.3 </td><td> 66.8 </td></tr>
<tr><td>Honda</td><td>Civic</td><td>1.3 Hybrid</td><td>2008</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 66.6 </td><td> 68.5 </td><td> 70.8 </td></tr>
<tr><td>Honda</td><td>Civic</td><td>1.3</td><td>2010</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 66.7 </td><td> 68.8 </td><td> 71.1 </td></tr>
<tr><td>Honda</td><td>Civic</td><td>Hybrid</td><td>2010</td><td> 45.5 </td><td> 59.1 </td><td> 65.1 </td><td> 66.1 </td><td> 70.1 </td><td> 73.1 </td></tr>
<tr><td>Honda</td><td>Civic</td><td>Hybrid</td><td>2011</td><td> 46.9 </td><td> 56.2 </td><td> 61.9 </td><td> 65.0 </td><td> 67.4 </td><td> 69.9 </td></tr>
<tr><td>Honda</td><td>Civic</td><td>1.8</td><td>2012</td><td> 37.7 </td><td> 59.8 </td><td> 64.1 </td><td> 69.4 </td><td> 71.1 </td><td> 73.2 </td></tr>
<tr><td>Honda</td><td>Civic</td><td>Si</td><td>2012</td><td> 43.8 </td><td> 55.3 </td><td> 62.5 </td><td> 66.1 </td><td> 70.0 </td><td> 73.9 </td></tr>
<tr><td>Honda</td><td>Civic</td><td>1.6 Stationcar</td><td>2014</td><td> 43.6 </td><td> 58.3 </td><td> 61.7 </td><td> 64.2 </td><td> 67.1 </td><td> 69.8 </td></tr>
<tr><td>Honda</td><td>Civic</td><td>1.8</td><td>2014</td><td> 39.7 </td><td> 53.1 </td><td> 61.3 </td><td> 66.2 </td><td> 68.0 </td><td> 69.8 </td></tr>
<tr><td>Honda</td><td>Civic</td><td>1.0</td><td>2017</td><td> 37.5 </td><td> 57.2 </td><td> 62.0 </td><td> 65.8 </td><td> 71.9 </td><td> 72.0 </td></tr>
<tr><td>Honda</td><td>CR-V</td><td>2.0</td><td>2008</td><td> 44.3 </td><td> 54.5 </td><td> 62.7 </td><td> 67.4 </td><td> 68.1 </td><td> 69.2 </td></tr>
<tr><td>Honda</td><td>CR-V</td><td>2.4</td><td>2012</td><td> 39.9 </td><td> 52.3 </td><td> 60.1 </td><td> 64.2 </td><td> 67.5 </td><td> 70.8 </td></tr>
<tr><td>Honda</td><td>CR-V</td><td>2.0</td><td>2013</td><td> 42.5 </td><td> 58.9 </td><td> 64.3 </td><td> 67.3 </td><td> 69.7 </td><td> 73.0 </td></tr>
<tr><td>Honda</td><td>CR-V</td><td>&nbsp;</td><td>2014</td><td> 46.4 </td><td> 56.6 </td><td> 61.7 </td><td> 63.8 </td><td> 66.7 </td><td> 69.0 </td></tr>
<tr><td>Honda</td><td>CR-V</td><td>1.6</td><td>2015</td><td> 44.2 </td><td> 55.8 </td><td> 60.8 </td><td> 63.1 </td><td> 68.1 </td><td> 70.9 </td></tr>
<tr><td>Honda</td><td>CR-Z</td><td>&nbsp;</td><td>2011</td><td> 40.5 </td><td> 54.3 </td><td> 62.9 </td><td> 67.6 </td><td> 70.5 </td><td> 73.4 </td></tr>
<tr><td>Honda</td><td>Fit</td><td>1.5 </td><td>2009</td><td> 42.4 </td><td> 56.2 </td><td> 64.7 </td><td> 69.6 </td><td> 71.9 </td><td> 74.2 </td></tr>
<tr><td>Honda</td><td>HR-V</td><td>1.5</td><td>2016</td><td> 36.7 </td><td> 56.2 </td><td> 60.6 </td><td> 64.6 </td><td> 67.0 </td><td> 71.3 </td></tr>
<tr><td>Honda</td><td>HR-V</td><td>1.5</td><td>2017</td><td> 39.9 </td><td> 59.8 </td><td> 63.0 </td><td> 66.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Honda</td><td>HR-V</td><td>1.6D</td><td>2017</td><td> 47.9 </td><td> 58.8 </td><td> 62.0 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Honda</td><td>Insight</td><td>1.3</td><td>2009</td><td> 35.3 </td><td> 59.0 </td><td> 62.9 </td><td> 67.3 </td><td> 68.8 </td><td> 73.3 </td></tr>
<tr><td>Honda</td><td>Insight</td><td>EX</td><td>2010</td><td> 44.4 </td><td> 56.5 </td><td> 63.9 </td><td> 68.4 </td><td> 69.5 </td><td> 70.7 </td></tr>
<tr><td>Honda</td><td>Insight</td><td>1.3</td><td>2012</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 66.2 </td><td> 68.3 </td><td> 70.6 </td></tr>
<tr><td>Honda</td><td>Jazz</td><td>1.2</td><td>2009</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 65.4 </td><td> 67.1 </td><td> 69.2 </td></tr>
<tr><td>Honda</td><td>Jazz</td><td>1.2</td><td>2010</td><td> 44.0 </td><td> 54.2 </td><td> 62.3 </td><td> 66.4 </td><td> 67.7 </td><td> 69.4 </td></tr>
<tr><td>Honda</td><td>Jazz</td><td>1.3 Hybrid</td><td>2011</td><td> 45.0 </td><td> 56.9 </td><td> 63.8 </td><td> 65.4 </td><td> 69.4 </td><td> 73.8 </td></tr>
<tr><td>Honda</td><td>Jazz</td><td>1.3</td><td>2016</td><td> 38.4 </td><td> 57.3 </td><td> 64.3 </td><td> 65.6 </td><td> 68.6 </td><td> 72.6 </td></tr>
<tr><td>Honda</td><td>Legend</td><td>3.7 V6</td><td>2009</td><td> 41.7 </td><td> 51.3 </td><td> 59.0 </td><td> 62.6 </td><td> 64.1 </td><td> 66.0 </td></tr>
<tr><td>Honda</td><td>NSX</td><td>3.5 V6</td><td>2017</td><td> 48.9 </td><td> 63.7 </td><td> 66.0 </td><td> 68.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Honda</td><td>Odyssey</td><td>3.5 V6</td><td>2011</td><td> 37.6 </td><td> 53.1 </td><td> 62.5 </td><td> 68.5 </td><td> 69.4 </td><td> 70.3 </td></tr>
<tr><td>Honda</td><td>Pilot</td><td>3.5 V6</td><td>2009</td><td> 43.0 </td><td> 55.4 </td><td> 62.9 </td><td> 67.3 </td><td> 69.4 </td><td> 71.4 </td></tr>
<tr><td>Hummer</td><td>H3</td><td>5.3 V8</td><td>2008</td><td> 50.9 </td><td> 59.4 </td><td> 65.2 </td><td> 66.7 </td><td> 74.0 </td><td> 81.3 </td></tr>
<tr><td>Hyundai</td><td>Accent</td><td>1.6</td><td>2012</td><td> 42.8 </td><td> 54.0 </td><td> 61.0 </td><td> 64.7 </td><td> 67.6 </td><td> 70.5 </td></tr>
<tr><td>Hyundai</td><td>Azera</td><td>3.3</td><td>2012</td><td> 38.9 </td><td> 50.6 </td><td> 57.9 </td><td> 61.6 </td><td> 65.3 </td><td> 69.0 </td></tr>
<tr><td>Hyundai</td><td>Coupe</td><td>2.7 V6</td><td>2008</td><td> 45.8 </td><td> 56.3 </td><td> 64.8 </td><td> 68.1 </td><td> 70.5 </td><td> 73.1 </td></tr>
<tr><td>Hyundai</td><td>Elantra</td><td>Stationcar</td><td>2009</td><td> 42.5 </td><td> 52.8 </td><td> 59.6 </td><td> 62.1 </td><td> 68.4 </td><td> 74.7 </td></tr>
<tr><td>Hyundai</td><td>Equues</td><td>4.6 V8</td><td>2011</td><td> 40.1 </td><td> 50.5 </td><td> 57.0 </td><td> 60.3 </td><td> 63.6 </td><td> 66.9 </td></tr>
<tr><td>Hyundai</td><td>Genesis</td><td>3.8 V6</td><td>2009</td><td> 40.0 </td><td> 51.6 </td><td> 58.7 </td><td> 62.8 </td><td> 65.0 </td><td> 67.2 </td></tr>
<tr><td>Hyundai</td><td>Genesis</td><td>&nbsp;</td><td>2010</td><td> 47.7 </td><td> 59.4 </td><td> 66.6 </td><td> 70.6 </td><td> 73.0 </td><td> 75.3 </td></tr>
<tr><td>Hyundai</td><td>Genesis</td><td>Coupe</td><td>2010</td><td> 43.7 </td><td> 54.9 </td><td> 62.0 </td><td> 65.1 </td><td> 70.1 </td><td> 75.2 </td></tr>
<tr><td>Hyundai</td><td>Genesis</td><td>3.8 V6</td><td>2011</td><td> 46.8 </td><td> 57.6 </td><td> 66.2 </td><td> 68.2 </td><td> 72.1 </td><td> 76.5 </td></tr>
<tr><td>Hyundai</td><td>Genesis</td><td>5.0</td><td>2012</td><td> 39.1 </td><td> 51.4 </td><td> 59.0 </td><td> 63.2 </td><td> 65.8 </td><td> 68.4 </td></tr>
<tr><td>Hyundai</td><td>Genesis</td><td>Coupe</td><td>2012</td><td> 43.0 </td><td> 54.1 </td><td> 61.4 </td><td> 64.2 </td><td> 70.2 </td><td> 76.1 </td></tr>
<tr><td>Hyundai</td><td>Genesis</td><td>3.8 V6</td><td>2013</td><td> 42.8 </td><td> 54.1 </td><td> 61.4 </td><td> 64.2 </td><td> 70.4 </td><td> 76.7 </td></tr>
<tr><td>Hyundai</td><td>i10</td><td>1.1</td><td>2008</td><td> 47.0 </td><td> 64.3 </td><td> 68.2 </td><td> 72.0 </td><td> 75.5 </td><td> 79.5 </td></tr>
<tr><td>Hyundai</td><td>i10</td><td>1.2</td><td>2011</td><td> 46.3 </td><td> 57.0 </td><td> 65.6 </td><td> 69.5 </td><td> 71.3 </td><td> 73.5 </td></tr>
<tr><td>Hyundai</td><td>i10</td><td>1.0</td><td>2013</td><td> 42.5 </td><td> 59.4 </td><td> 63.4 </td><td> 65.7 </td><td> 69.8 </td><td> 72.4 </td></tr>
<tr><td>Hyundai</td><td>i10</td><td>1.0</td><td>2014</td><td> 42.5 </td><td> 59.4 </td><td> 63.4 </td><td> 65.7 </td><td> 69.8 </td><td> 72.4 </td></tr>
<tr><td>Hyundai</td><td>i10</td><td>1.0</td><td>2016</td><td> 40.9 </td><td> 58.8 </td><td> 62.5 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Hyundai</td><td>i20</td><td>1.1</td><td>2008</td><td> 45.9 </td><td> 56.5 </td><td> 65.0 </td><td> 69.0 </td><td> 70.6 </td><td> 72.6 </td></tr>
<tr><td>Hyundai</td><td>i20</td><td>1.2</td><td>2009</td><td> 47.2 </td><td> 58.1 </td><td> 66.8 </td><td> 70.1 </td><td> 72.7 </td><td> 75.7 </td></tr>
<tr><td>Hyundai</td><td>i20</td><td>1.4</td><td>2009</td><td> 40.7 </td><td> 61.1 </td><td> 66.9 </td><td> 69.4 </td><td> 72.5 </td><td> 74.5 </td></tr>
<tr><td>Hyundai</td><td>i20</td><td>1.2</td><td>2010</td><td> 37.4 </td><td> 62.3 </td><td> 66.1 </td><td> 68.5 </td><td> 69.8 </td><td> 72.6 </td></tr>
<tr><td>Hyundai</td><td>i20</td><td>1.2</td><td>2012</td><td> 46.8 </td><td> 57.6 </td><td> 66.2 </td><td> 68.1 </td><td> 72.1 </td><td> 76.6 </td></tr>
<tr><td>Hyundai</td><td>i20</td><td>1.2</td><td>2015</td><td> 37.0 </td><td> 61.0 </td><td> 63.6 </td><td> 65.9 </td><td> 66.9 </td><td> 68.7 </td></tr>
<tr><td>Hyundai</td><td>i20</td><td>1.0</td><td>2016</td><td> 38.9 </td><td> 59.8 </td><td> 63.5 </td><td> 67.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Hyundai</td><td>i20</td><td>1.0</td><td>2017</td><td> 38.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Hyundai</td><td>i30</td><td>2.0</td><td>2008</td><td> 45.1 </td><td> 55.5 </td><td> 63.8 </td><td> 67.2 </td><td> 69.5 </td><td> 72.0 </td></tr>
<tr><td>Hyundai</td><td>i30</td><td>1.4</td><td>2010</td><td> 45.6 </td><td> 56.2 </td><td> 64.6 </td><td> 67.9 </td><td> 70.3 </td><td> 72.9 </td></tr>
<tr><td>Hyundai</td><td>i30</td><td>1.6</td><td>2012</td><td> 44.2 </td><td> 57.8 </td><td> 64.2 </td><td> 65.2 </td><td> 68.1 </td><td> 72.1 </td></tr>
<tr><td>Hyundai</td><td>i30</td><td>1.6</td><td>2012</td><td> 44.6 </td><td> 54.9 </td><td> 63.1 </td><td> 66.0 </td><td> 68.7 </td><td> 71.8 </td></tr>
<tr><td>Hyundai</td><td>i30</td><td>1.6 GDi</td><td>2012</td><td> 45.4 </td><td> 58.9 </td><td> 64.2 </td><td> 66.9 </td><td> 70.0 </td><td> 73.1 </td></tr>
<tr><td>Hyundai</td><td>i30</td><td>1.6</td><td>2013</td><td> 43.4 </td><td> 53.4 </td><td> 61.5 </td><td> 65.0 </td><td> 66.8 </td><td> 69.0 </td></tr>
<tr><td>Hyundai</td><td>i30</td><td>1.0</td><td>2017</td><td> 34.4 </td><td> 55.7 </td><td> 60.8 </td><td> 63.9 </td><td> 69.9 </td><td> 70.0 </td></tr>
<tr><td>Hyundai</td><td>i30</td><td>1.4</td><td>2017</td><td> 40.9 </td><td> 55.8 </td><td> 60.5 </td><td> 65.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Hyundai</td><td>i30</td><td>1.4 stationcar</td><td>2017</td><td> 34.3 </td><td> 56.6 </td><td> 60.2 </td><td> 63.7 </td><td> 70.6 </td><td> 70.7 </td></tr>
<tr><td>Hyundai</td><td>i40</td><td>1.6 GDI</td><td>2011</td><td> 34.7 </td><td> 56.8 </td><td> 60.6 </td><td> 64.5 </td><td> 68.4 </td><td> 71.8 </td></tr>
<tr><td>Hyundai</td><td>i40</td><td>1.6 Stationcar</td><td>2011</td><td> 44.3 </td><td> 54.5 </td><td> 62.7 </td><td> 65.4 </td><td> 68.2 </td><td> 71.4 </td></tr>
<tr><td>Hyundai</td><td>i40</td><td>1.7 CRDI</td><td>2012</td><td> 45.4 </td><td> 55.9 </td><td> 64.3 </td><td> 67.7 </td><td> 70.0 </td><td> 72.5 </td></tr>
<tr><td>Hyundai</td><td>i40</td><td>1.6 Stationcar</td><td>2013</td><td> 44.4 </td><td> 56.8 </td><td> 60.6 </td><td> 64.5 </td><td> 68.4 </td><td> 71.8 </td></tr>
<tr><td>Hyundai</td><td>i40</td><td>1.7 D</td><td>2015</td><td> 46.6 </td><td> 59.7 </td><td> 63.1 </td><td> 65.7 </td><td> 68.3 </td><td> 71.7 </td></tr>
<tr><td>Hyundai</td><td>Ioniq</td><td>1.6 Hybrid</td><td>2016</td><td> 31.5 </td><td> 56.2 </td><td> 60.2 </td><td> 63.3 </td><td> 68.5 </td><td> 70.6 </td></tr>
<tr><td>Hyundai</td><td>Ioniq</td><td>EV</td><td>2017</td><td> 45.2 </td><td> 54.7 </td><td> 59.8 </td><td> 63.2 </td><td> 69.6 </td><td> 69.7 </td></tr>
<tr><td>Hyundai</td><td>ix20</td><td>1.4 CRD</td><td>2011</td><td> 46.0 </td><td> 56.6 </td><td> 65.0 </td><td> 67.2 </td><td> 70.8 </td><td> 74.9 </td></tr>
<tr><td>Hyundai</td><td>ix20</td><td>1.4 CRDI</td><td>2011</td><td> 46.0 </td><td> 56.6 </td><td> 65.0 </td><td> 67.2 </td><td> 70.8 </td><td> 74.9 </td></tr>
<tr><td>Hyundai</td><td>IX35</td><td>2.0 CRDI</td><td>2010</td><td> 44.3 </td><td> 58.5 </td><td> 62.9 </td><td> 66.7 </td><td> 68.2 </td><td> 70.5 </td></tr>
<tr><td>Hyundai</td><td>IX35</td><td>1.6 GDI</td><td>2012</td><td> 35.6 </td><td> 55.4 </td><td> 62.6 </td><td> 65.0 </td><td> 68.7 </td><td> 72.0 </td></tr>
<tr><td>Hyundai</td><td>Santa Fe</td><td>2.2 CRDI</td><td>2010</td><td> 43.2 </td><td> 53.1 </td><td> 61.1 </td><td> 64.3 </td><td> 66.5 </td><td> 68.9 </td></tr>
<tr><td>Hyundai</td><td>Sonata</td><td>2.0</td><td>2009</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 67.9 </td><td> 68.3 </td><td> 69.0 </td></tr>
<tr><td>Hyundai</td><td>Sonata</td><td>2.0T</td><td>2011</td><td> 38.2 </td><td> 50.0 </td><td> 57.2 </td><td> 61.6 </td><td> 62.8 </td><td> 64.1 </td></tr>
<tr><td>Hyundai</td><td>Sonata</td><td>2.4</td><td>2011</td><td> 43.1 </td><td> 55.0 </td><td> 62.3 </td><td> 66.6 </td><td> 68.3 </td><td> 70.1 </td></tr>
<tr><td>Hyundai</td><td>Sonata</td><td>Hybrid</td><td>2011</td><td> 38.4 </td><td> 50.4 </td><td> 57.9 </td><td> 61.6 </td><td> 65.9 </td><td> 70.3 </td></tr>
<tr><td>Hyundai</td><td>Tucson</td><td>2.4</td><td>2010</td><td> 40.6 </td><td> 54.4 </td><td> 62.8 </td><td> 67.9 </td><td> 69.3 </td><td> 70.8 </td></tr>
<tr><td>Hyundai</td><td>Tucson</td><td>2.4</td><td>2014</td><td> 43.5 </td><td> 54.2 </td><td> 60.7 </td><td> 64.6 </td><td> 66.1 </td><td> 67.7 </td></tr>
<tr><td>Hyundai</td><td>Tucson</td><td>1.6</td><td>2015</td><td> 33.5 </td><td> 53.8 </td><td> 59.9 </td><td> 62.6 </td><td> 67.0 </td><td> 70.2 </td></tr>
<tr><td>Hyundai</td><td>Tucson</td><td>1.6</td><td>2016</td><td> 33.9 </td><td> 56.8 </td><td> 60.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Hyundai</td><td>Tucson</td><td>2.0D</td><td>2016</td><td> 48.9 </td><td> 60.8 </td><td> 63.0 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Hyundai</td><td>Velostar</td><td>1.6</td><td>2011</td><td> 44.7 </td><td> 55.0 </td><td> 63.3 </td><td> 67.3 </td><td> 68.8 </td><td> 70.7 </td></tr>
<tr><td>Hyundai</td><td>Veloster</td><td>I-Catcher 1.6</td><td>2011</td><td> 45.2 </td><td> 59.2 </td><td> 63.4 </td><td> 66.3 </td><td> 69.7 </td><td> 73.8 </td></tr>
<tr><td>Hyundai</td><td>Veloster</td><td>1.6</td><td>2012</td><td> 39.6 </td><td> 52.7 </td><td> 60.9 </td><td> 65.3 </td><td> 68.6 </td><td> 72.0 </td></tr>
<tr><td>Infinity</td><td>EX</td><td>35</td><td>2008</td><td> 41.7 </td><td> 55.1 </td><td> 63.5 </td><td> 68.0 </td><td> 71.3 </td><td> 74.7 </td></tr>
<tr><td>Infinity</td><td>EX</td><td>37</td><td>2009</td><td> 43.1 </td><td> 53.0 </td><td> 61.0 </td><td> 64.9 </td><td> 66.3 </td><td> 68.1 </td></tr>
<tr><td>Infinity</td><td>FX</td><td>50</td><td>2009</td><td> 49.6 </td><td> 59.7 </td><td> 65.8 </td><td> 69.5 </td><td> 70.8 </td><td> 72.2 </td></tr>
<tr><td>Infinity</td><td>G</td><td>37</td><td>2008</td><td> 45.0 </td><td> 55.5 </td><td> 62.1 </td><td> 65.4 </td><td> 68.8 </td><td> 72.2 </td></tr>
<tr><td>Infinity</td><td>G</td><td>37</td><td>2009</td><td> 43.7 </td><td> 53.8 </td><td> 61.9 </td><td> 65.5 </td><td> 67.3 </td><td> 69.5 </td></tr>
<tr><td>Infinity</td><td>G</td><td>37S Coupe</td><td>2009</td><td> 41.1 </td><td> 60.0 </td><td> 64.0 </td><td> 65.5 </td><td> 68.4 </td><td> 70.0 </td></tr>
<tr><td>Infinity</td><td>G</td><td>37 Cabrio</td><td>2010</td><td> 42.8 </td><td> 52.7 </td><td> 60.6 </td><td> 64.4 </td><td> 65.9 </td><td> 67.8 </td></tr>
<tr><td>Infinity</td><td>G</td><td>25</td><td>2011</td><td> 47.6 </td><td> 55.6 </td><td> 60.7 </td><td> 63.1 </td><td> 66.0 </td><td> 69.0 </td></tr>
<tr><td>Infinity</td><td>JX</td><td>35</td><td>2012</td><td> 41.0 </td><td> 52.0 </td><td> 58.8 </td><td> 62.3 </td><td> 65.6 </td><td> 68.9 </td></tr>
<tr><td>Infinity</td><td>M</td><td>37</td><td>2011</td><td> 42.9 </td><td> 55.6 </td><td> 63.4 </td><td> 67.8 </td><td> 70.3 </td><td> 72.8 </td></tr>
<tr><td>Infinity</td><td>M</td><td>30D</td><td>2011</td><td> 44.2 </td><td> 60.1 </td><td> 61.3 </td><td> 64.2 </td><td> 66.6 </td><td> 71.0 </td></tr>
<tr><td>Infinity</td><td>M</td><td>37S</td><td>2011</td><td> 44.6 </td><td> 56.5 </td><td> 63.8 </td><td> 67.9 </td><td> 70.2 </td><td> 72.5 </td></tr>
<tr><td>Infinity</td><td>M</td><td>56S</td><td>2011</td><td> 42.2 </td><td> 53.9 </td><td> 61.2 </td><td> 65.2 </td><td> 67.7 </td><td> 70.3 </td></tr>
<tr><td>Infinity</td><td>M</td><td>35H</td><td>2012</td><td> 38.5 </td><td> 53.3 </td><td> 57.2 </td><td> 61.3 </td><td> 65.4 </td><td> 67.8 </td></tr>
<tr><td>Infinity</td><td>M</td><td>35H</td><td>2012</td><td> 42.2 </td><td> 53.0 </td><td> 59.8 </td><td> 63.3 </td><td> 66.4 </td><td> 69.6 </td></tr>
<tr><td>Infinity</td><td>Q</td><td>50</td><td>2013</td><td> 38.4 </td><td> 50.4 </td><td> 57.8 </td><td> 61.9 </td><td> 64.6 </td><td> 67.3 </td></tr>
<tr><td>Infinity</td><td>Q</td><td>50</td><td>2014</td><td> 49.4 </td><td> 56.6 </td><td> 60.4 </td><td> 61.8 </td><td> 65.9 </td><td> 69.3 </td></tr>
<tr><td>Infinity</td><td>Q</td><td>70</td><td>2015</td><td> 44.6 </td><td> 57.5 </td><td> 60.0 </td><td> 63.0 </td><td> 66.0 </td><td> 70.0 </td></tr>
<tr><td>Infinity</td><td>Q30</td><td>1.5D</td><td>2016</td><td> 45.4 </td><td> 56.3 </td><td> 61.3 </td><td> 64.2 </td><td> 67.8 </td><td> 71.2 </td></tr>
<tr><td>Infinity</td><td>Q30</td><td>2.0</td><td>2016</td><td> 41.9 </td><td> 56.8 </td><td> 60.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Infinity</td><td>QX</td><td>56</td><td>2011</td><td> 43.3 </td><td> 54.6 </td><td> 61.5 </td><td> 65.6 </td><td> 67.1 </td><td> 68.6 </td></tr>
<tr><td>Infinity</td><td>QX</td><td>60</td><td>2013</td><td> 41.1 </td><td> 51.5 </td><td> 58.0 </td><td> 61.3 </td><td> 64.3 </td><td> 67.4 </td></tr>
<tr><td>Infinity</td><td>QX50</td><td>3.7 V6</td><td>2016</td><td> 41.2 </td><td> 53.3 </td><td> 60.6 </td><td> 65.1 </td><td> 66.3 </td><td> 67.5 </td></tr>
<tr><td>Jaguar</td><td>F-Pace</td><td>3.0 V6</td><td>2016</td><td> 40.4 </td><td> 57.3 </td><td> 62.0 </td><td> 64.6 </td><td> 66.0 </td><td> 69.6 </td></tr>
<tr><td>Jaguar</td><td>F-Pace</td><td>3.0D</td><td>2016</td><td> 47.9 </td><td> 58.8 </td><td> 61.5 </td><td> 64.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Jaguar</td><td>F-Pace</td><td>2.0d</td><td>2017</td><td> 44.5 </td><td> 53.6 </td><td> 58.6 </td><td> 61.7 </td><td> 68.5 </td><td> 68.6 </td></tr>
<tr><td>Jaguar</td><td>F-Type</td><td>5.0 V8</td><td>2014</td><td> 46.5 </td><td> 55.2 </td><td> 61.0 </td><td> 63.0 </td><td> 68.8 </td><td> 74.6 </td></tr>
<tr><td>Jaguar</td><td>F-Type</td><td>5.0 V8</td><td>2017</td><td> 44.9 </td><td> 61.8 </td><td> 65.0 </td><td> 68.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Jaguar</td><td>XE</td><td>2.0D</td><td>2015</td><td> 45.2 </td><td> 56.2 </td><td> 63.1 </td><td> 65.2 </td><td> 67.0 </td><td> 70.1 </td></tr>
<tr><td>Jaguar</td><td>XE</td><td>2.0D</td><td>2016</td><td> 43.2 </td><td> 57.7 </td><td> 60.6 </td><td> 63.8 </td><td> 67.7 </td><td> 69.7 </td></tr>
<tr><td>Jaguar</td><td>XE</td><td>3.0D</td><td>2016</td><td> 50.8 </td><td> 58.8 </td><td> 61.0 </td><td> 63.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Jaguar</td><td>XF</td><td>2.7d</td><td>2008</td><td> 47.7 </td><td> 55.1 </td><td> 60.1 </td><td> 63.6 </td><td> 66.6 </td><td> 69.6 </td></tr>
<tr><td>Jaguar</td><td>XF</td><td>3.0 V6</td><td>2008</td><td> 40.8 </td><td> 61.4 </td><td> 62.4 </td><td> 64.0 </td><td> 66.7 </td><td> 69.1 </td></tr>
<tr><td>Jaguar</td><td>XF</td><td>3.0D S</td><td>2009</td><td> 45.4 </td><td> 57.1 </td><td> 61.2 </td><td> 64.0 </td><td> 66.6 </td><td> 69.0 </td></tr>
<tr><td>Jaguar</td><td>XF</td><td>3.0 V6</td><td>2010</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 66.5 </td><td> 68.3 </td><td> 70.5 </td></tr>
<tr><td>Jaguar</td><td>XF</td><td>2.2 D</td><td>2011</td><td> 43.0 </td><td> 52.9 </td><td> 60.8 </td><td> 64.8 </td><td> 66.1 </td><td> 67.8 </td></tr>
<tr><td>Jaguar</td><td>XF</td><td>2.2D</td><td>2011</td><td> 43.0 </td><td> 52.9 </td><td> 60.8 </td><td> 64.8 </td><td> 66.1 </td><td> 67.8 </td></tr>
<tr><td>Jaguar</td><td>XF</td><td>2.0</td><td>2016</td><td> 44.2 </td><td> 59.5 </td><td> 63.0 </td><td> 64.0 </td><td> 66.0 </td><td> 68.0 </td></tr>
<tr><td>Jaguar</td><td>XF</td><td>3.0D</td><td>2016</td><td> 48.1 </td><td> 57.2 </td><td> 60.7 </td><td> 64.3 </td><td> 67.3 </td><td> 70.7 </td></tr>
<tr><td>Jaguar</td><td>XF</td><td>2.0d</td><td>2017</td><td> 45.2 </td><td> 54.5 </td><td> 58.3 </td><td> 62.6 </td><td> 68.9 </td><td> 69.0 </td></tr>
<tr><td>Jaguar</td><td>XFR</td><td>5.0 V8 Supercharged</td><td>2010</td><td> 45.6 </td><td> 56.3 </td><td> 62.9 </td><td> 66.6 </td><td> 68.7 </td><td> 70.8 </td></tr>
<tr><td>Jaguar</td><td>XF-S</td><td>&nbsp;</td><td>2009</td><td> 47.0 </td><td> 57.3 </td><td> 63.6 </td><td> 67.3 </td><td> 68.7 </td><td> 70.2 </td></tr>
<tr><td>Jaguar</td><td>XJ</td><td>3.0D V6</td><td>2010</td><td> 43.5 </td><td> 53.5 </td><td> 61.5 </td><td> 64.6 </td><td> 67.0 </td><td> 69.6 </td></tr>
<tr><td>Jaguar</td><td>XJ</td><td>5.0 V8 LWB</td><td>2010</td><td> 39.9 </td><td> 59.0 </td><td> 61.0 </td><td> 62.7 </td><td> 66.6 </td><td> 68.0 </td></tr>
<tr><td>Jaguar</td><td>XJ</td><td>5.0 V8</td><td>2014</td><td> 40.6 </td><td> 50.3 </td><td> 56.5 </td><td> 59.2 </td><td> 63.3 </td><td> 67.5 </td></tr>
<tr><td>Jaguar</td><td>XK</td><td>3.5 V6</td><td>2008</td><td> 43.0 </td><td> 53.0 </td><td> 60.9 </td><td> 64.7 </td><td> 66.2 </td><td> 68.1 </td></tr>
<tr><td>Jaguar</td><td>XK</td><td>5.0 V8 Convertible </td><td>2011</td><td> 44.3 </td><td> 54.5 </td><td> 62.7 </td><td> 65.1 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Jaguar</td><td>XKR-S</td><td>5.0 V8</td><td>2012</td><td> 44.8 </td><td> 55.1 </td><td> 63.4 </td><td> 66.7 </td><td> 69.0 </td><td> 71.5 </td></tr>
<tr><td>Jaguar</td><td>X-type</td><td>2.2D</td><td>2008</td><td> 43.6 </td><td> 53.6 </td><td> 61.6 </td><td> 64.8 </td><td> 67.1 </td><td> 69.6 </td></tr>
<tr><td>Jeep</td><td>Cherokee</td><td>2.0</td><td>2014</td><td> 47.3 </td><td> 59.8 </td><td> 62.8 </td><td> 64.2 </td><td> 66.6 </td><td> 68.6 </td></tr>
<tr><td>Jeep</td><td>Compass</td><td>2.4</td><td>2011</td><td> 45.2 </td><td> 55.6 </td><td> 63.9 </td><td> 67.2 </td><td> 69.6 </td><td> 72.2 </td></tr>
<tr><td>Jeep</td><td>Grand Cherokee</td><td>CRD</td><td>2008</td><td> 48.4 </td><td> 57.7 </td><td> 63.4 </td><td> 66.6 </td><td> 68.7 </td><td> 70.9 </td></tr>
<tr><td>Jeep</td><td>Grand Cherokee</td><td>Hennessey</td><td>2008</td><td> 53.1 </td><td> 62.1 </td><td> 67.9 </td><td> 70.2 </td><td> 75.1 </td><td> 80.0 </td></tr>
<tr><td>Jeep</td><td>Grand Cherokee</td><td>3.6 V6</td><td>2011</td><td> 43.7 </td><td> 53.8 </td><td> 61.8 </td><td> 66.3 </td><td> 67.2 </td><td> 68.5 </td></tr>
<tr><td>Jeep</td><td>Grand Cherokee</td><td>SRT8</td><td>2012</td><td> 48.7 </td><td> 56.7 </td><td> 61.9 </td><td> 64.0 </td><td> 68.2 </td><td> 72.3 </td></tr>
<tr><td>Jeep</td><td>Grand Cherokee</td><td>3.6 V6</td><td>2014</td><td> 51.2 </td><td> 57.3 </td><td> 61.0 </td><td> 63.1 </td><td> 64.3 </td><td> 65.6 </td></tr>
<tr><td>Jeep</td><td>Renegade</td><td>1.4</td><td>2015</td><td> 37.7 </td><td> 56.2 </td><td> 60.1 </td><td> 63.5 </td><td> 66.9 </td><td> 71.6 </td></tr>
<tr><td>Jeep</td><td>Wrangler</td><td>3.8 V6</td><td>2008</td><td> 45.5 </td><td> 56.0 </td><td> 64.4 </td><td> 67.2 </td><td> 70.1 </td><td> 73.4 </td></tr>
<tr><td>Jeep</td><td>Wrangler</td><td>3.6 V6</td><td>2012</td><td> 47.5 </td><td> 57.9 </td><td> 64.5 </td><td> 67.5 </td><td> 71.7 </td><td> 76.0 </td></tr>
<tr><td>Kia</td><td>Carens</td><td>2.0</td><td>2008</td><td> 44.1 </td><td> 54.2 </td><td> 62.4 </td><td> 66.1 </td><td> 67.8 </td><td> 69.9 </td></tr>
<tr><td>Kia</td><td>Carens</td><td>2.0</td><td>2013</td><td> 44.3 </td><td> 57.3 </td><td> 62.0 </td><td> 64.5 </td><td> 68.3 </td><td> 69.3 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>1.6</td><td>2008</td><td> 37.4 </td><td> 60.5 </td><td> 64.3 </td><td> 67.3 </td><td> 69.4 </td><td> 72.2 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>1.4</td><td>2008</td><td> 40.1 </td><td> 59.0 </td><td> 65.0 </td><td> 65.5 </td><td> 68.0 </td><td> 71.0 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>1.6 Stationcar</td><td>2008</td><td> 45.6 </td><td> 56.2 </td><td> 64.6 </td><td> 67.1 </td><td> 70.3 </td><td> 73.9 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>2.0</td><td>2008</td><td> 45.5 </td><td> 56.0 </td><td> 64.4 </td><td> 68.2 </td><td> 70.0 </td><td> 72.2 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>2.0 Stationcar</td><td>2008</td><td> 44.8 </td><td> 55.1 </td><td> 63.4 </td><td> 66.5 </td><td> 69.0 </td><td> 71.9 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>1.4 Stationcar</td><td>2009</td><td> 45.0 </td><td> 55.4 </td><td> 63.8 </td><td> 67.2 </td><td> 69.4 </td><td> 71.8 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>1.6</td><td>2010</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 67.1 </td><td> 68.7 </td><td> 70.7 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>1.6</td><td>2012</td><td> 44.8 </td><td> 55.1 </td><td> 63.4 </td><td> 66.1 </td><td> 69.0 </td><td> 72.3 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>1.6</td><td>2014</td><td> 44.0 </td><td> 59.2 </td><td> 64.7 </td><td> 65.3 </td><td> 67.7 </td><td> 71.8 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>1.0</td><td>2016</td><td> 40.1 </td><td> 58.2 </td><td> 61.2 </td><td> 64.3 </td><td> 66.3 </td><td> 69.7 </td></tr>
<tr><td>Kia</td><td>Cee'd</td><td>1.0 Stationcar</td><td>2016</td><td> 37.7 </td><td> 54.2 </td><td> 58.6 </td><td> 62.5 </td><td> 65.7 </td><td> 67.8 </td></tr>
<tr><td>Kia</td><td>Forte</td><td>SX</td><td>2010</td><td> 43.8 </td><td> 52.8 </td><td> 58.5 </td><td> 61.2 </td><td> 64.6 </td><td> 68.0 </td></tr>
<tr><td>Kia</td><td>Niro</td><td>1.6</td><td>2016</td><td> 35.3 </td><td> 56.3 </td><td> 60.5 </td><td> 63.7 </td><td> 67.0 </td><td> 69.1 </td></tr>
<tr><td>Kia</td><td>Optima</td><td>Hybrid</td><td>2011</td><td> 37.9 </td><td> 52.5 </td><td> 61.4 </td><td> 66.7 </td><td> 68.5 </td><td> 70.2 </td></tr>
<tr><td>Kia</td><td>Optima</td><td>SX Turbo</td><td>2011</td><td> 44.2 </td><td> 53.9 </td><td> 59.9 </td><td> 63.3 </td><td> 65.2 </td><td> 67.1 </td></tr>
<tr><td>Kia</td><td>Optima</td><td>1.7D</td><td>2012</td><td> 44.3 </td><td> 58.8 </td><td> 63.6 </td><td> 66.7 </td><td> 68.2 </td><td> 71.6 </td></tr>
<tr><td>Kia</td><td>Optima</td><td>2.0 Hybrid</td><td>2013</td><td> 43.1 </td><td> 53.0 </td><td> 61.0 </td><td> 64.1 </td><td> 66.4 </td><td> 68.9 </td></tr>
<tr><td>Kia</td><td>Optima</td><td>1.7D</td><td>2016</td><td> 45.5 </td><td> 56.1 </td><td> 60.2 </td><td> 64.6 </td><td> 66.7 </td><td> 70.1 </td></tr>
<tr><td>Kia</td><td>Optima</td><td>1.7d</td><td>2017</td><td> 45.9 </td><td> 57.8 </td><td> 61.0 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Kia</td><td>Optima</td><td>2.0</td><td>2017</td><td> 44.0 </td><td> 52.6 </td><td> 57.8 </td><td> 61.5 </td><td> 67.8 </td><td> 67.9 </td></tr>
<tr><td>Kia</td><td>Picanto</td><td>1.1</td><td>2008</td><td> 47.3 </td><td> 58.2 </td><td> 67.0 </td><td> 69.8 </td><td> 72.9 </td><td> 76.4 </td></tr>
<tr><td>Kia</td><td>Picanto</td><td>1.0</td><td>2011</td><td> 46.0 </td><td> 56.6 </td><td> 65.0 </td><td> 68.6 </td><td> 70.8 </td><td> 73.2 </td></tr>
<tr><td>Kia</td><td>Picanto</td><td>1.2</td><td>2012</td><td> 46.3 </td><td> 58.8 </td><td> 64.2 </td><td> 66.9 </td><td> 71.4 </td><td> 73.5 </td></tr>
<tr><td>Kia</td><td>Picanto</td><td>1.0</td><td>2013</td><td> 39.5 </td><td> 57.9 </td><td> 63.3 </td><td> 67.2 </td><td> 70.7 </td><td> 73.7 </td></tr>
<tr><td>Kia</td><td>Pro Cee'd</td><td>GT</td><td>2014</td><td> 38.8 </td><td> 56.3 </td><td> 62.2 </td><td> 65.0 </td><td> 68.2 </td><td> 70.7 </td></tr>
<tr><td>Kia</td><td>Pro_CEE'D</td><td>1.6</td><td>2013</td><td> 39.2 </td><td> 57.9 </td><td> 63.6 </td><td> 66.3 </td><td> 70.5 </td><td> 74.1 </td></tr>
<tr><td>Kia</td><td>Rio</td><td>1.2</td><td>2011</td><td> 36.5 </td><td> 60.6 </td><td> 66.7 </td><td> 69.6 </td><td> 71.9 </td><td> 74.9 </td></tr>
<tr><td>Kia</td><td>Rio</td><td>1.2</td><td>2011</td><td> 43.2 </td><td> 53.2 </td><td> 61.2 </td><td> 65.4 </td><td> 66.5 </td><td> 68.0 </td></tr>
<tr><td>Kia</td><td>Rio</td><td>1.2 </td><td>2012</td><td> 39.1 </td><td> 61.2 </td><td> 66.2 </td><td> 68.0 </td><td> 71.3 </td><td> 74.0 </td></tr>
<tr><td>Kia</td><td>Rio</td><td>1.0</td><td>2017</td><td> 39.4 </td><td> 57.5 </td><td> 61.7 </td><td> 64.7 </td><td> 69.7 </td><td> 69.7 </td></tr>
<tr><td>Kia</td><td>Sorento</td><td>2.4</td><td>2010</td><td> 44.0 </td><td> 54.2 </td><td> 62.3 </td><td> 66.3 </td><td> 67.7 </td><td> 69.5 </td></tr>
<tr><td>Kia</td><td>Sorento</td><td>EX V6</td><td>2011</td><td> 34.5 </td><td> 46.6 </td><td> 54.0 </td><td> 58.2 </td><td> 60.6 </td><td> 63.0 </td></tr>
<tr><td>Kia</td><td>Sorento</td><td>V6</td><td>2011</td><td> 34.5 </td><td> 46.6 </td><td> 54.0 </td><td> 58.2 </td><td> 60.6 </td><td> 63.0 </td></tr>
<tr><td>Kia</td><td>Soul</td><td>&nbsp;</td><td>2009</td><td> 39.2 </td><td> 61.2 </td><td> 66.0 </td><td> 68.9 </td><td> 72.3 </td><td> 74.9 </td></tr>
<tr><td>Kia</td><td>Soul</td><td>1.6</td><td>2009</td><td> 44.8 </td><td> 55.1 </td><td> 63.4 </td><td> 65.4 </td><td> 69.0 </td><td> 73.1 </td></tr>
<tr><td>Kia</td><td>Soul</td><td>&nbsp;</td><td>2010</td><td> 44.3 </td><td> 56.7 </td><td> 64.4 </td><td> 68.5 </td><td> 71.5 </td><td> 74.5 </td></tr>
<tr><td>Kia</td><td>Soul</td><td>1.6</td><td>2015</td><td> 43.6 </td><td> 58.2 </td><td> 62.6 </td><td> 66.9 </td><td> 69.6 </td><td> 71.3 </td></tr>
<tr><td>Kia</td><td>Soul</td><td>EV</td><td>2017</td><td> 44.8 </td><td> 56.2 </td><td> 60.2 </td><td> 63.2 </td><td> 69.0 </td><td> 69.0 </td></tr>
<tr><td>Kia</td><td>Sportage</td><td>2.0</td><td>2010</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 68.5 </td><td> 69.2 </td><td> 70.3 </td></tr>
<tr><td>Kia</td><td>Sportage</td><td>2.4</td><td>2011</td><td> 42.9 </td><td> 56.7 </td><td> 65.0 </td><td> 70.3 </td><td> 71.2 </td><td> 72.1 </td></tr>
<tr><td>Kia</td><td>Sportage</td><td>1.6</td><td>2012</td><td> 35.4 </td><td> 56.2 </td><td> 63.6 </td><td> 65.2 </td><td> 69.3 </td><td> 71.7 </td></tr>
<tr><td>Kia</td><td>Sportage</td><td>1.6</td><td>2012</td><td> 46.3 </td><td> 57.0 </td><td> 65.5 </td><td> 69.0 </td><td> 71.3 </td><td> 73.8 </td></tr>
<tr><td>Kia</td><td>Sportage</td><td>1.6 </td><td>2012</td><td> 44.6 </td><td> 59.7 </td><td> 65.3 </td><td> 65.8 </td><td> 68.6 </td><td> 71.3 </td></tr>
<tr><td>Kia</td><td>Sportage</td><td>1.6</td><td>2016</td><td> 44.4 </td><td> 55.6 </td><td> 59.8 </td><td> 62.9 </td><td> 66.3 </td><td> 68.4 </td></tr>
<tr><td>Kia</td><td>Stonic</td><td>1.0</td><td>2017</td><td> 37.1 </td><td> 56.3 </td><td> 61.3 </td><td> 63.9 </td><td> 70.9 </td><td> 71.0 </td></tr>
<tr><td>Kia</td><td>Venga</td><td>1.4</td><td>2010</td><td> 42.1 </td><td> 63.0 </td><td> 66.5 </td><td> 69.0 </td><td> 72.0 </td><td> 75.0 </td></tr>
<tr><td>Kia</td><td>Venga</td><td>1.4</td><td>2010</td><td> 44.1 </td><td> 54.3 </td><td> 62.5 </td><td> 67.4 </td><td> 67.9 </td><td> 68.7 </td></tr>
<tr><td>Lancia</td><td>Delta</td><td>1.4</td><td>2008</td><td> 43.7 </td><td> 60.4 </td><td> 66.8 </td><td> 68.3 </td><td> 70.9 </td><td> 73.3 </td></tr>
<tr><td>Lancia</td><td>Delta</td><td>1.9D</td><td>2009</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 65.1 </td><td> 67.2 </td><td> 69.5 </td></tr>
<tr><td>Lancia</td><td>Delta</td><td>1.8</td><td>2010</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 68.0 </td><td> 69.2 </td><td> 70.8 </td></tr>
<tr><td>Lancia</td><td>Delta</td><td>1.4</td><td>2011</td><td> 43.6 </td><td> 56.8 </td><td> 61.4 </td><td> 64.0 </td><td> 67.2 </td><td> 70.8 </td></tr>
<tr><td>Lancia</td><td>Thema</td><td>3.6 V6</td><td>2012</td><td> 41.3 </td><td> 50.9 </td><td> 58.5 </td><td> 63.0 </td><td> 63.6 </td><td> 64.5 </td></tr>
<tr><td>Lancia</td><td>Ypsilon</td><td>0.9</td><td>2011</td><td> 46.3 </td><td> 57.6 </td><td> 62.7 </td><td> 66.5 </td><td> 71.4 </td><td> 73.0 </td></tr>
<tr><td>Lancia</td><td>Ypsilon</td><td>0.9</td><td>2011</td><td> 46.2 </td><td> 56.8 </td><td> 65.3 </td><td> 68.7 </td><td> 71.1 </td><td> 73.7 </td></tr>
<tr><td>Lancia</td><td>Ypsilon</td><td>0.9</td><td>2013</td><td> 42.3 </td><td> 58.3 </td><td> 62.7 </td><td> 66.0 </td><td> 70.4 </td><td> 74.2 </td></tr>
<tr><td>Land Rover</td><td>Discovery</td><td>3.0 TD V6</td><td>2010</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 66.7 </td><td> 68.8 </td><td> 71.1 </td></tr>
<tr><td>Land Rover</td><td>Discovery</td><td>2.2</td><td>2015</td><td> 45.8 </td><td> 55.3 </td><td> 59.9 </td><td> 63.6 </td><td> 66.1 </td><td> 70.4 </td></tr>
<tr><td>Land Rover</td><td>Discovery</td><td>2.0D</td><td>2016</td><td> 46.1 </td><td> 61.2 </td><td> 63.8 </td><td> 66.3 </td><td> 68.3 </td><td> 71.8 </td></tr>
<tr><td>Land Rover</td><td>Discovery</td><td>2.0d</td><td>2017</td><td> 46.9 </td><td> 60.8 </td><td> 64.0 </td><td> 67.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Land Rover</td><td>Discovery Sport</td><td>2.0</td><td>2017</td><td> 37.0 </td><td> 55.1 </td><td> 57.5 </td><td> 60.3 </td><td> 67.3 </td><td> 67.3 </td></tr>
<tr><td>Land Rover</td><td>Freelander</td><td>2.2D</td><td>2008</td><td> 48.1 </td><td> 59.2 </td><td> 63.0 </td><td> 66.0 </td><td> 67.6 </td><td> 71.0 </td></tr>
<tr><td>Land Rover</td><td>Freelander</td><td>TD4</td><td>2008</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 65.9 </td><td> 67.5 </td><td> 69.5 </td></tr>
<tr><td>Land Rover</td><td>Freelander</td><td>TD4</td><td>2009</td><td> 43.5 </td><td> 53.5 </td><td> 61.5 </td><td> 64.7 </td><td> 67.0 </td><td> 69.5 </td></tr>
<tr><td>Land Rover</td><td>Freelander</td><td>2.2D</td><td>2011</td><td> 46.4 </td><td> 59.1 </td><td> 63.0 </td><td> 66.1 </td><td> 69.2 </td><td> 71.6 </td></tr>
<tr><td>Lexus</td><td>CT</td><td>200h</td><td>2011</td><td> 44.9 </td><td> 60.9 </td><td> 62.8 </td><td> 65.4 </td><td> 69.0 </td><td> 71.5 </td></tr>
<tr><td>Lexus</td><td>CT</td><td>200h</td><td>2012</td><td> 45.0 </td><td> 56.7 </td><td> 61.3 </td><td> 65.2 </td><td> 68.4 </td><td> 71.5 </td></tr>
<tr><td>Lexus</td><td>CT</td><td>200h</td><td>2014</td><td> 43.5 </td><td> 55.2 </td><td> 60.7 </td><td> 63.5 </td><td> 67.0 </td><td> 70.8 </td></tr>
<tr><td>Lexus</td><td>ES</td><td>300h</td><td>2012</td><td> 41.0 </td><td> 50.7 </td><td> 56.6 </td><td> 59.9 </td><td> 62.0 </td><td> 64.0 </td></tr>
<tr><td>Lexus</td><td>GS</td><td>480h</td><td>2009</td><td> 42.3 </td><td> 52.0 </td><td> 59.8 </td><td> 62.6 </td><td> 65.1 </td><td> 67.9 </td></tr>
<tr><td>Lexus</td><td>GS</td><td>350F</td><td>2012</td><td> 40.0 </td><td> 51.6 </td><td> 58.7 </td><td> 62.9 </td><td> 64.8 </td><td> 66.8 </td></tr>
<tr><td>Lexus</td><td>GS</td><td>450h</td><td>2012</td><td> 41.2 </td><td> 52.4 </td><td> 57.2 </td><td> 58.6 </td><td> 62.8 </td><td> 67.2 </td></tr>
<tr><td>Lexus</td><td>GS</td><td>300h</td><td>2014</td><td> 41.2 </td><td> 49.5 </td><td> 53.4 </td><td> 57.3 </td><td> 60.8 </td><td> 63.8 </td></tr>
<tr><td>Lexus</td><td>GS</td><td>450h</td><td>2017</td><td> 41.9 </td><td> 55.8 </td><td> 59.0 </td><td> 62.2 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Lexus</td><td>GX</td><td>460</td><td>2010</td><td> 42.3 </td><td> 53.8 </td><td> 60.8 </td><td> 64.9 </td><td> 66.8 </td><td> 68.8 </td></tr>
<tr><td>Lexus</td><td>HS</td><td>250h</td><td>2010</td><td> 44.2 </td><td> 54.1 </td><td> 60.3 </td><td> 63.6 </td><td> 65.9 </td><td> 68.3 </td></tr>
<tr><td>Lexus</td><td>IS</td><td>250</td><td>2008</td><td> 37.0 </td><td> 61.0 </td><td> 64.0 </td><td> 65.5 </td><td> 67.4 </td><td> 71.4 </td></tr>
<tr><td>Lexus</td><td>IS</td><td>F</td><td>2008</td><td> 47.6 </td><td> 57.1 </td><td> 63.1 </td><td> 65.9 </td><td> 69.9 </td><td> 73.9 </td></tr>
<tr><td>Lexus</td><td>IS</td><td>250C</td><td>2010</td><td> 38.4 </td><td> 58.7 </td><td> 63.1 </td><td> 66.2 </td><td> 69.3 </td><td> 71.4 </td></tr>
<tr><td>Lexus</td><td>IS</td><td>250C</td><td>2010</td><td> 43.2 </td><td> 53.2 </td><td> 61.2 </td><td> 64.0 </td><td> 66.6 </td><td> 69.6 </td></tr>
<tr><td>Lexus</td><td>IS</td><td>350C</td><td>2010</td><td> 44.4 </td><td> 55.4 </td><td> 62.4 </td><td> 65.9 </td><td> 69.2 </td><td> 72.5 </td></tr>
<tr><td>Lexus</td><td>IS</td><td>250h</td><td>2013</td><td> 41.6 </td><td> 52.9 </td><td> 59.8 </td><td> 63.7 </td><td> 66.0 </td><td> 68.4 </td></tr>
<tr><td>Lexus</td><td>IS</td><td>300h</td><td>2013</td><td> 43.9 </td><td> 54.1 </td><td> 60.0 </td><td> 62.6 </td><td> 65.9 </td><td> 69.3 </td></tr>
<tr><td>Lexus</td><td>LS</td><td>600h</td><td>2008</td><td> 38.7 </td><td> 48.6 </td><td> 54.8 </td><td> 58.1 </td><td> 60.4 </td><td> 62.8 </td></tr>
<tr><td>Lexus</td><td>LS</td><td>600h L</td><td>2009</td><td> 32.9 </td><td> 54.5 </td><td> 60.2 </td><td> 61.2 </td><td> 63.1 </td><td> 66.7 </td></tr>
<tr><td>Lexus</td><td>LS</td><td>600h L</td><td>2010</td><td> 41.2 </td><td> 54.1 </td><td> 58.1 </td><td> 60.9 </td><td> 63.6 </td><td> 66.5 </td></tr>
<tr><td>Lexus</td><td>LS</td><td>600h</td><td>2013</td><td> 35.4 </td><td> 47.5 </td><td> 54.9 </td><td> 59.3 </td><td> 60.8 </td><td> 62.3 </td></tr>
<tr><td>Lexus</td><td>LS</td><td>600h</td><td>2016</td><td> 40.9 </td><td> 53.8 </td><td> 56.5 </td><td> 59.2 </td><td> 61.3 </td><td> 64.5 </td></tr>
<tr><td>Lexus</td><td>NX</td><td>300h</td><td>2014</td><td> 34.3 </td><td> 53.2 </td><td> 57.8 </td><td> 60.9 </td><td> 63.6 </td><td> 66.6 </td></tr>
<tr><td>Lexus</td><td>RC</td><td>300h</td><td>2016</td><td> 30.2 </td><td> 56.3 </td><td> 60.8 </td><td> 63.5 </td><td> 65.1 </td><td> 67.7 </td></tr>
<tr><td>Lexus</td><td>RX</td><td>450h</td><td>2010</td><td> 40.2 </td><td> 52.1 </td><td> 59.5 </td><td> 63.6 </td><td> 66.1 </td><td> 68.6 </td></tr>
<tr><td>Lexus</td><td>RX</td><td>450h</td><td>2011</td><td> 44.1 </td><td> 54.3 </td><td> 62.5 </td><td> 65.6 </td><td> 68.0 </td><td> 70.6 </td></tr>
<tr><td>Lexus</td><td>RX</td><td>350</td><td>2013</td><td> 40.9 </td><td> 52.8 </td><td> 60.0 </td><td> 64.4 </td><td> 66.0 </td><td> 67.6 </td></tr>
<tr><td>Lexus</td><td>RX</td><td>450h</td><td>2016</td><td> 32.1 </td><td> 52.1 </td><td> 56.3 </td><td> 59.8 </td><td> 63.1 </td><td> 65.2 </td></tr>
<tr><td>Lincoln</td><td>MKS</td><td>3.7 V6</td><td>2009</td><td> 44.5 </td><td> 54.3 </td><td> 60.5 </td><td> 63.6 </td><td> 66.6 </td><td> 69.6 </td></tr>
<tr><td>Lincoln</td><td>MKT</td><td>3.5 V6</td><td>2010</td><td> 39.3 </td><td> 49.5 </td><td> 55.8 </td><td> 59.5 </td><td> 61.0 </td><td> 62.5 </td></tr>
<tr><td>Lincoln</td><td>MKX</td><td>3.7 V6</td><td>2016</td><td> 40.2 </td><td> 52.6 </td><td> 60.1 </td><td> 64.8 </td><td> 65.7 </td><td> 66.6 </td></tr>
<tr><td>Lincoln</td><td>MKZ</td><td>2.0</td><td>2012</td><td> 41.9 </td><td> 52.5 </td><td> 59.1 </td><td> 62.6 </td><td> 65.4 </td><td> 68.3 </td></tr>
<tr><td>Lotus</td><td>Elise</td><td>SC</td><td>2008</td><td> 56.0 </td><td> 67.2 </td><td> 74.2 </td><td> 77.7 </td><td> 81.3 </td><td> 84.8 </td></tr>
<tr><td>Lotus</td><td>Elise</td><td>1.8</td><td>2014</td><td> 49.4 </td><td> 69.2 </td><td> 72.6 </td><td> 75.9 </td><td> 82.3 </td><td> 84.3 </td></tr>
<tr><td>Lotus</td><td>Evora</td><td>3.5 V6</td><td>2011</td><td> 48.9 </td><td> 60.2 </td><td> 69.3 </td><td> 73.8 </td><td> 75.3 </td><td> 77.2 </td></tr>
<tr><td>Mazda</td><td>2</td><td>1.3</td><td>2008</td><td> 45.6 </td><td> 56.1 </td><td> 64.5 </td><td> 68.0 </td><td> 70.2 </td><td> 72.6 </td></tr>
<tr><td>Mazda</td><td>2</td><td>1.3</td><td>2011</td><td> 43.0 </td><td> 52.9 </td><td> 60.8 </td><td> 65.2 </td><td> 66.1 </td><td> 67.3 </td></tr>
<tr><td>Mazda</td><td>2</td><td>1.3</td><td>2011</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 67.1 </td><td> 68.0 </td><td> 69.3 </td></tr>
<tr><td>Mazda</td><td>2</td><td>1.3 BiFuel</td><td>2011</td><td> 44.8 </td><td> 57.3 </td><td> 62.3 </td><td> 65.7 </td><td> 69.0 </td><td> 72.3 </td></tr>
<tr><td>Mazda</td><td>2</td><td>1.5</td><td>2011</td><td> 40.9 </td><td> 56.8 </td><td> 66.4 </td><td> 72.3 </td><td> 74.1 </td><td> 75.9 </td></tr>
<tr><td>Mazda</td><td>2</td><td>1.5</td><td>2012</td><td> 44.3 </td><td> 56.0 </td><td> 63.3 </td><td> 67.4 </td><td> 69.5 </td><td> 71.7 </td></tr>
<tr><td>Mazda</td><td>2</td><td>1.5</td><td>2015</td><td> 45.6 </td><td> 56.9 </td><td> 62.7 </td><td> 67.2 </td><td> 70.2 </td><td> 73.2 </td></tr>
<tr><td>Mazda</td><td>2</td><td>1.5</td><td>2017</td><td> 38.6 </td><td> 56.8 </td><td> 61.2 </td><td> 64.9 </td><td> 72.0 </td><td> 72.1 </td></tr>
<tr><td>Mazda</td><td>3</td><td>1.6</td><td>2010</td><td> 46.0 </td><td> 56.6 </td><td> 65.0 </td><td> 67.7 </td><td> 70.8 </td><td> 74.3 </td></tr>
<tr><td>Mazda</td><td>3</td><td>2.3</td><td>2010</td><td> 44.7 </td><td> 57.0 </td><td> 64.6 </td><td> 68.9 </td><td> 71.4 </td><td> 74.0 </td></tr>
<tr><td>Mazda</td><td>3</td><td>Stationcar</td><td>2010</td><td> 43.3 </td><td> 55.5 </td><td> 63.1 </td><td> 67.3 </td><td> 69.8 </td><td> 72.4 </td></tr>
<tr><td>Mazda</td><td>3</td><td>1.6 CITD</td><td>2011</td><td> 44.7 </td><td> 55.0 </td><td> 63.3 </td><td> 67.0 </td><td> 68.8 </td><td> 71.0 </td></tr>
<tr><td>Mazda</td><td>3</td><td>1.6 CITD</td><td>2011</td><td> 44.7 </td><td> 55.0 </td><td> 63.3 </td><td> 67.0 </td><td> 68.8 </td><td> 71.0 </td></tr>
<tr><td>Mazda</td><td>3</td><td>2.0</td><td>2012</td><td> 38.3 </td><td> 58.0 </td><td> 63.2 </td><td> 67.2 </td><td> 70.8 </td><td> 73.2 </td></tr>
<tr><td>Mazda</td><td>3</td><td>2.0</td><td>2014</td><td> 38.5 </td><td> 60.5 </td><td> 65.4 </td><td> 68.3 </td><td> 70.9 </td><td> 73.2 </td></tr>
<tr><td>Mazda</td><td>3</td><td>2.5</td><td>2014</td><td> 40.5 </td><td> 53.4 </td><td> 61.2 </td><td> 65.8 </td><td> 67.8 </td><td> 69.8 </td></tr>
<tr><td>Mazda</td><td>3</td><td>2.5</td><td>2015</td><td> 40.5 </td><td> 52.4 </td><td> 59.8 </td><td> 63.9 </td><td> 66.3 </td><td> 68.7 </td></tr>
<tr><td>Mazda</td><td>5</td><td>2.0 CITD</td><td>2008</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 66.7 </td><td> 67.5 </td><td> 68.7 </td></tr>
<tr><td>Mazda</td><td>5</td><td>1.6 CITD</td><td>2011</td><td> 43.5 </td><td> 53.5 </td><td> 61.5 </td><td> 64.6 </td><td> 67.0 </td><td> 69.6 </td></tr>
<tr><td>Mazda</td><td>5</td><td>2.0</td><td>2011</td><td> 45.5 </td><td> 61.0 </td><td> 64.5 </td><td> 67.0 </td><td> 70.0 </td><td> 73.0 </td></tr>
<tr><td>Mazda</td><td>5</td><td>Stationcar</td><td>2012</td><td> 42.9 </td><td> 54.1 </td><td> 60.9 </td><td> 65.0 </td><td> 66.2 </td><td> 67.4 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.0 CITD</td><td>2008</td><td> 48.5 </td><td> 59.2 </td><td> 65.1 </td><td> 67.1 </td><td> 72.1 </td><td> 73.6 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.0 CITD Stationcar</td><td>2008</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 67.1 </td><td> 69.0 </td><td> 71.3 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.0 Stationcar</td><td>2008</td><td> 43.8 </td><td> 53.9 </td><td> 62.0 </td><td> 64.5 </td><td> 67.5 </td><td> 70.9 </td></tr>
<tr><td>Mazda</td><td>6</td><td>Stationcar</td><td>2009</td><td> 44.8 </td><td> 55.6 </td><td> 62.5 </td><td> 65.8 </td><td> 69.7 </td><td> 73.6 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.2 CiTD Stationcar</td><td>2011</td><td> 43.1 </td><td> 53.0 </td><td> 61.0 </td><td> 65.0 </td><td> 66.3 </td><td> 68.0 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.2 CiTD Stationcar</td><td>2011</td><td> 43.1 </td><td> 53.0 </td><td> 61.0 </td><td> 65.0 </td><td> 66.3 </td><td> 68.0 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.0 Stationcar</td><td>2013</td><td> 38.9 </td><td> 58.8 </td><td> 62.2 </td><td> 65.7 </td><td> 67.3 </td><td> 70.6 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.5</td><td>2013</td><td> 41.2 </td><td> 51.7 </td><td> 58.4 </td><td> 61.7 </td><td> 65.0 </td><td> 68.3 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.5 V6</td><td>2013</td><td> 41.2 </td><td> 51.7 </td><td> 58.4 </td><td> 61.7 </td><td> 65.0 </td><td> 68.3 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.2D Stationcar</td><td>2015</td><td> 43.1 </td><td> 57.0 </td><td> 62.1 </td><td> 65.7 </td><td> 68.7 </td><td> 71.4 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.5</td><td>2016</td><td> 37.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.2d</td><td>2017</td><td> 43.9 </td><td> 59.8 </td><td> 63.5 </td><td> 67.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Mazda</td><td>6</td><td>2.2d stationcar</td><td>2017</td><td> 40.1 </td><td> 56.4 </td><td> 60.3 </td><td> 63.4 </td><td> 69.7 </td><td> 69.7 </td></tr>
<tr><td>Mazda</td><td>CX3</td><td>2.0</td><td>2016</td><td> 38.5 </td><td> 55.0 </td><td> 62.2 </td><td> 65.4 </td><td> 69.2 </td><td> 71.6 </td></tr>
<tr><td>Mazda</td><td>CX-3</td><td>2</td><td>2015</td><td> 43.6 </td><td> 59.2 </td><td> 63.1 </td><td> 66.9 </td><td> 69.6 </td><td> 71.3 </td></tr>
<tr><td>Mazda</td><td>CX-3</td><td>2.0</td><td>2017</td><td> 34.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Mazda</td><td>CX-5</td><td>2.0</td><td>2012</td><td> 46.2 </td><td> 60.5 </td><td> 65.4 </td><td> 68.9 </td><td> 71.2 </td><td> 72.7 </td></tr>
<tr><td>Mazda</td><td>CX-5</td><td>2.0</td><td>2012</td><td> 37.3 </td><td> 56.4 </td><td> 62.2 </td><td> 65.2 </td><td> 68.4 </td><td> 72.2 </td></tr>
<tr><td>Mazda</td><td>CX-5</td><td>2.0</td><td>2012</td><td> 43.9 </td><td> 55.3 </td><td> 62.3 </td><td> 66.3 </td><td> 68.4 </td><td> 70.6 </td></tr>
<tr><td>Mazda</td><td>CX-5</td><td>2.0</td><td>2012</td><td> 45.6 </td><td> 56.1 </td><td> 64.5 </td><td> 68.6 </td><td> 70.1 </td><td> 72.0 </td></tr>
<tr><td>Mazda</td><td>CX-5</td><td>2.0</td><td>2013</td><td> 37.0 </td><td> 51.5 </td><td> 58.9 </td><td> 63.7 </td><td> 66.9 </td><td> 69.7 </td></tr>
<tr><td>Mazda</td><td>CX-5</td><td>2.2</td><td>2015</td><td> 44.2 </td><td> 55.8 </td><td> 61.0 </td><td> 64.1 </td><td> 68.1 </td><td> 71.9 </td></tr>
<tr><td>Mazda</td><td>CX-5</td><td>2.0</td><td>2017</td><td> 44.9 </td><td> 58.8 </td><td> 61.5 </td><td> 64.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Mazda</td><td>CX-5</td><td>2.2d</td><td>2017</td><td> 49.9 </td><td> 54.8 </td><td> 59.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Mazda</td><td>MX-5</td><td>2'.0</td><td>2012</td><td> 44.5 </td><td> 54.7 </td><td> 62.9 </td><td> 67.3 </td><td> 68.4 </td><td> 69.9 </td></tr>
<tr><td>Mazda</td><td>MX-5</td><td>1.5</td><td>2016</td><td> 42.9 </td><td> 62.7 </td><td> 67.5 </td><td> 72.3 </td><td> 75.0 </td><td> 78.8 </td></tr>
<tr><td>Mazda</td><td>MX-5</td><td>2.0</td><td>2016</td><td> 48.5 </td><td> 62.2 </td><td> 69.6 </td><td> 74.0 </td><td> 78.6 </td><td> 80.7 </td></tr>
<tr><td>McLaren</td><td>570S</td><td>3.8 V8</td><td>2017</td><td> 59.8 </td><td> 70.7 </td><td> 72.0 </td><td> 73.3 </td><td> 75.0 </td><td> 78.8 </td></tr>
<tr><td>McLaren</td><td>MP4-12C</td><td>3.8 V8</td><td>2012</td><td> 60.5 </td><td> 65.9 </td><td> 69.8 </td><td> 70.2 </td><td> 76.9 </td><td> 83.6 </td></tr>
<tr><td>Mercedes</td><td>A</td><td>180</td><td>2012</td><td> 39.0 </td><td> 54.3 </td><td> 60.1 </td><td> 63.1 </td><td> 66.2 </td><td> 70.8 </td></tr>
<tr><td>Mercedes</td><td>A</td><td>200</td><td>2012</td><td> 40.3 </td><td> 55.0 </td><td> 59.9 </td><td> 63.2 </td><td> 66.7 </td><td> 69.6 </td></tr>
<tr><td>Mercedes</td><td>A</td><td>180d</td><td>2016</td><td> 46.9 </td><td> 58.8 </td><td> 62.5 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Mercedes</td><td>A</td><td>45 AMG</td><td>2016</td><td> 49.9 </td><td> 60.8 </td><td> 63.5 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Mercedes</td><td>AMG GT</td><td>R</td><td>2017</td><td> 52.8 </td><td> 63.7 </td><td> 67.5 </td><td> 69.0 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>Mercedes</td><td>B</td><td>200</td><td>2012</td><td> 43.4 </td><td> 58.8 </td><td> 62.5 </td><td> 66.2 </td><td> 66.8 </td><td> 69.1 </td></tr>
<tr><td>Mercedes</td><td>B</td><td>200</td><td>2012</td><td> 45.0 </td><td> 55.4 </td><td> 63.8 </td><td> 67.3 </td><td> 69.4 </td><td> 71.7 </td></tr>
<tr><td>Mercedes</td><td>B</td><td>180</td><td>2014</td><td> 41.4 </td><td> 55.1 </td><td> 58.9 </td><td> 61.7 </td><td> 64.9 </td><td> 67.6 </td></tr>
<tr><td>Mercedes</td><td>B</td><td>EV</td><td>2017</td><td> 43.2 </td><td> 54.3 </td><td> 59.2 </td><td> 61.5 </td><td> 66.5 </td><td> 66.5 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>180</td><td>2008</td><td> 41.8 </td><td> 51.4 </td><td> 59.2 </td><td> 62.2 </td><td> 64.4 </td><td> 66.8 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>350</td><td>2008</td><td> 43.8 </td><td> 54.3 </td><td> 60.8 </td><td> 64.1 </td><td> 67.3 </td><td> 70.5 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>200 CDI</td><td>2008</td><td> 47.7 </td><td> 57.6 </td><td> 62.1 </td><td> 65.6 </td><td> 68.1 </td><td> 72.1 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>220 CDI Stationcar</td><td>2008</td><td> 44.0 </td><td> 54.2 </td><td> 62.3 </td><td> 65.5 </td><td> 67.8 </td><td> 70.3 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>63 AMG</td><td>2008</td><td> 49.2 </td><td> 58.6 </td><td> 64.5 </td><td> 67.4 </td><td> 70.5 </td><td> 73.6 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>250 CDI</td><td>2009</td><td> 45.6 </td><td> 56.1 </td><td> 64.5 </td><td> 68.6 </td><td> 70.1 </td><td> 72.0 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>180</td><td>2011</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 66.1 </td><td> 69.1 </td><td> 72.5 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>180</td><td>2011</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 66.1 </td><td> 69.1 </td><td> 72.5 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>250</td><td>2012</td><td> 45.7 </td><td> 53.5 </td><td> 58.5 </td><td> 60.8 </td><td> 63.9 </td><td> 67.1 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>63 AMG</td><td>2012</td><td> 48.8 </td><td> 57.6 </td><td> 63.2 </td><td> 65.7 </td><td> 69.7 </td><td> 73.8 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>220</td><td>2014</td><td> 48.3 </td><td> 54.8 </td><td> 59.2 </td><td> 62.2 </td><td> 65.4 </td><td> 69.4 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>300</td><td>2014</td><td> 42.5 </td><td> 52.2 </td><td> 58.4 </td><td> 61.1 </td><td> 65.6 </td><td> 70.2 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>180 Stationcar</td><td>2015</td><td> 46.4 </td><td> 57.8 </td><td> 62.2 </td><td> 64.2 </td><td> 66.4 </td><td> 69.3 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>250 Stationcar</td><td>2015</td><td> 42.3 </td><td> 57.2 </td><td> 61.1 </td><td> 64.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Mercedes</td><td>C</td><td>250 Coupe</td><td>2016</td><td> 42.4 </td><td> 57.5 </td><td> 62.2 </td><td> 63.7 </td><td> 66.0 </td><td> 68.3 </td></tr>
<tr><td>Mercedes</td><td>C </td><td>220 Stationcar</td><td>2014</td><td> 40.3 </td><td> 56.2 </td><td> 59.1 </td><td> 61.9 </td><td> 65.7 </td><td> 67.3 </td></tr>
<tr><td>Mercedes</td><td>C </td><td>350E</td><td>2015</td><td> 41.5 </td><td> 53.5 </td><td> 57.3 </td><td> 62.6 </td><td> 66.1 </td><td> 69.4 </td></tr>
<tr><td>Mercedes</td><td>C </td><td>450 AMG</td><td>2015</td><td> 43.6 </td><td> 58.2 </td><td> 62.6 </td><td> 66.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Mercedes</td><td>CL</td><td>500/550</td><td>2011</td><td> 41.7 </td><td> 51.9 </td><td> 58.1 </td><td> 61.7 </td><td> 63.6 </td><td> 65.6 </td></tr>
<tr><td>Mercedes</td><td>CLA</td><td>200</td><td>2013</td><td> 39.3 </td><td> 56.5 </td><td> 61.2 </td><td> 65.5 </td><td> 67.6 </td><td> 70.7 </td></tr>
<tr><td>Mercedes</td><td>CLA</td><td>200</td><td>2014</td><td> 46.6 </td><td> 55.7 </td><td> 61.6 </td><td> 64.0 </td><td> 68.5 </td><td> 73.0 </td></tr>
<tr><td>Mercedes</td><td>CLA</td><td>250</td><td>2014</td><td> 42.2 </td><td> 53.6 </td><td> 60.7 </td><td> 64.4 </td><td> 67.6 </td><td> 70.9 </td></tr>
<tr><td>Mercedes</td><td>CLA</td><td>45 AMG</td><td>2014</td><td> 47.1 </td><td> 61.2 </td><td> 63.8 </td><td> 66.3 </td><td> 67.3 </td><td> 70.7 </td></tr>
<tr><td>Mercedes</td><td>CLA</td><td>180</td><td>2016</td><td> 40.1 </td><td> 56.0 </td><td> 59.4 </td><td> 62.8 </td><td> 66.5 </td><td> 68.5 </td></tr>
<tr><td>Mercedes</td><td>CLC</td><td>180</td><td>2008</td><td> 43.7 </td><td> 53.8 </td><td> 61.8 </td><td> 64.8 </td><td> 67.3 </td><td> 70.0 </td></tr>
<tr><td>Mercedes</td><td>CLS</td><td>350</td><td>2011</td><td> 41.9 </td><td> 51.6 </td><td> 59.3 </td><td> 62.1 </td><td> 64.6 </td><td> 67.4 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>300</td><td>2008</td><td> 41.7 </td><td> 51.4 </td><td> 59.1 </td><td> 62.8 </td><td> 64.2 </td><td> 66.0 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>63 AMG</td><td>2008</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 66.3 </td><td> 68.4 </td><td> 70.7 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>250 CDI</td><td>2009</td><td> 43.3 </td><td> 53.3 </td><td> 61.3 </td><td> 64.3 </td><td> 66.7 </td><td> 69.3 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>350 CDI</td><td>2009</td><td> 39.1 </td><td> 54.9 </td><td> 59.4 </td><td> 62.6 </td><td> 65.4 </td><td> 68.3 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>350 CGI Coupe</td><td>2009</td><td> 42.8 </td><td> 52.7 </td><td> 60.6 </td><td> 64.3 </td><td> 65.9 </td><td> 67.9 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>250 CGI Cabrio</td><td>2010</td><td> 41.9 </td><td> 58.9 </td><td> 62.1 </td><td> 65.7 </td><td> 67.1 </td><td> 69.9 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>350 CDI</td><td>2010</td><td> 39.1 </td><td> 54.9 </td><td> 59.4 </td><td> 62.6 </td><td> 65.4 </td><td> 68.3 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>350 CGI Stationcar</td><td>2010</td><td> 43.4 </td><td> 53.4 </td><td> 61.4 </td><td> 65.8 </td><td> 66.7 </td><td> 68.0 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>500/550</td><td>2010</td><td> 44.2 </td><td> 55.4 </td><td> 62.3 </td><td> 66.2 </td><td> 68.4 </td><td> 70.7 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>550/500 Coupe</td><td>2010</td><td> 45.2 </td><td> 52.7 </td><td> 57.4 </td><td> 59.6 </td><td> 62.6 </td><td> 65.5 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>63 AMG</td><td>2010</td><td> 43.1 </td><td> 49.2 </td><td> 53.5 </td><td> 54.4 </td><td> 60.2 </td><td> 66.0 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>350 CGI Stationcar</td><td>2011</td><td> 39.8 </td><td> 58.0 </td><td> 63.0 </td><td> 65.1 </td><td> 67.3 </td><td> 70.0 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>350</td><td>2012</td><td> 43.4 </td><td> 53.4 </td><td> 61.5 </td><td> 64.4 </td><td> 66.9 </td><td> 69.6 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>200</td><td>2014</td><td> 39.8 </td><td> 53.3 </td><td> 56.8 </td><td> 60.3 </td><td> 63.4 </td><td> 67.4 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>350</td><td>2014</td><td> 38.2 </td><td> 49.0 </td><td> 55.8 </td><td> 59.2 </td><td> 62.6 </td><td> 66.0 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>220d</td><td>2016</td><td> 42.4 </td><td> 52.1 </td><td> 56.6 </td><td> 59.6 </td><td> 62.1 </td><td> 65.3 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>220d Stationcar</td><td>2016</td><td> 43.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>250 Stationcar</td><td>2016</td><td> 42.2 </td><td> 54.2 </td><td> 58.8 </td><td> 61.5 </td><td> 66.4 </td><td> 68.5 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>350d</td><td>2016</td><td> 42.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>220d</td><td>2017</td><td> 43.7 </td><td> 53.5 </td><td> 58.2 </td><td> 60.6 </td><td> 67.5 </td><td> 67.5 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>350d</td><td>2017</td><td> 41.9 </td><td> 56.8 </td><td> 60.5 </td><td> 64.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>350d stationcar</td><td>2017</td><td> 40.9 </td><td> 57.8 </td><td> 60.5 </td><td> 63.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Mercedes</td><td>E</td><td>400</td><td>2017</td><td> 36.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Mercedes</td><td>E 220</td><td>2.1D</td><td>2015</td><td> 41.6 </td><td> 56.2 </td><td> 60.1 </td><td> 63.9 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>Mercedes</td><td>E 250</td><td>2.1D</td><td>2015</td><td> 42.3 </td><td> 58.2 </td><td> 61.6 </td><td> 64.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Mercedes</td><td>E 350</td><td>Convertible</td><td>2013</td><td> 41.6 </td><td> 57.2 </td><td> 60.6 </td><td> 63.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Mercedes</td><td>E 350</td><td>&nbsp;</td><td>2015</td><td> 41.0 </td><td> 55.2 </td><td> 59.1 </td><td> 62.9 </td><td> 65.7 </td><td> 67.3 </td></tr>
<tr><td>Mercedes</td><td>GLA</td><td>200</td><td>2014</td><td> 41.3 </td><td> 58.3 </td><td> 60.9 </td><td> 65.2 </td><td> 66.7 </td><td> 70.0 </td></tr>
<tr><td>Mercedes</td><td>GLA</td><td>250</td><td>2015</td><td> 42.3 </td><td> 59.2 </td><td> 62.1 </td><td> 64.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Mercedes</td><td>GLA</td><td>45 AMG</td><td>2015</td><td> 43.6 </td><td> 59.2 </td><td> 63.1 </td><td> 66.9 </td><td> 69.6 </td><td> 71.3 </td></tr>
<tr><td>Mercedes</td><td>GLC</td><td>250d</td><td>2015</td><td> 43.4 </td><td> 54.3 </td><td> 57.7 </td><td> 61.9 </td><td> 64.3 </td><td> 68.3 </td></tr>
<tr><td>Mercedes</td><td>GLC</td><td>250d</td><td>2016</td><td> 43.1 </td><td> 59.2 </td><td> 62.2 </td><td> 65.3 </td><td> 66.3 </td><td> 69.7 </td></tr>
<tr><td>Mercedes</td><td>GLC</td><td>250d</td><td>2016</td><td> 42.9 </td><td> 55.8 </td><td> 59.5 </td><td> 62.7 </td><td> 64.2 </td><td> 67.5 </td></tr>
<tr><td>Mercedes</td><td>GLC</td><td>250d</td><td>2017</td><td> 44.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Mercedes</td><td>GLC</td><td>350d</td><td>2017</td><td> 40.7 </td><td> 53.8 </td><td> 57.1 </td><td> 59.6 </td><td> 64.8 </td><td> 64.8 </td></tr>
<tr><td>Mercedes</td><td>GLC</td><td>43 AMG</td><td>2017</td><td> 40.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Mercedes</td><td>GLE</td><td>250d</td><td>2016</td><td> 44.9 </td><td> 56.8 </td><td> 59.5 </td><td> 62.2 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Mercedes</td><td>GLE</td><td> 400</td><td>2017</td><td> 38.9 </td><td> 55.8 </td><td> 59.0 </td><td> 62.2 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Mercedes</td><td>GLE</td><td>350d</td><td>2017</td><td> 43.9 </td><td> 56.8 </td><td> 60.5 </td><td> 64.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Mercedes</td><td>GLK</td><td>320 CDI</td><td>2008</td><td> 46.1 </td><td> 57.6 </td><td> 61.1 </td><td> 66.7 </td><td> 68.1 </td><td> 70.3 </td></tr>
<tr><td>Mercedes</td><td>GLK</td><td>220 CDI</td><td>2009</td><td> 42.8 </td><td> 52.7 </td><td> 60.6 </td><td> 63.5 </td><td> 66.0 </td><td> 68.7 </td></tr>
<tr><td>Mercedes</td><td>GLK</td><td>220</td><td>2014</td><td> 41.6 </td><td> 56.2 </td><td> 60.1 </td><td> 63.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Mercedes</td><td>GLK</td><td>3.0D V6</td><td>2014</td><td> 42.3 </td><td> 57.2 </td><td> 61.1 </td><td> 64.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Mercedes</td><td>ML</td><td>63 AMG</td><td>2008</td><td> 42.4 </td><td> 52.2 </td><td> 60.0 </td><td> 63.7 </td><td> 65.2 </td><td> 67.1 </td></tr>
<tr><td>Mercedes</td><td>ML</td><td>320</td><td>2009</td><td> 46.0 </td><td> 55.3 </td><td> 60.9 </td><td> 64.3 </td><td> 65.5 </td><td> 66.7 </td></tr>
<tr><td>Mercedes</td><td>ML</td><td>350</td><td>2012</td><td> 43.6 </td><td> 54.1 </td><td> 59.1 </td><td> 62.9 </td><td> 67.1 </td><td> 69.2 </td></tr>
<tr><td>Mercedes</td><td>ML</td><td>350</td><td>2012</td><td> 42.1 </td><td> 51.8 </td><td> 59.5 </td><td> 62.0 </td><td> 64.8 </td><td> 68.0 </td></tr>
<tr><td>Mercedes</td><td>ML</td><td>450/500</td><td>2012</td><td> 41.1 </td><td> 51.0 </td><td> 57.1 </td><td> 60.6 </td><td> 62.3 </td><td> 64.0 </td></tr>
<tr><td>Mercedes</td><td>R</td><td>350 CDI</td><td>2012</td><td> 42.3 </td><td> 52.1 </td><td> 59.9 </td><td> 62.8 </td><td> 65.2 </td><td> 67.8 </td></tr>
<tr><td>Mercedes</td><td>S</td><td>500</td><td>2008</td><td> 42.9 </td><td> 52.8 </td><td> 60.7 </td><td> 62.1 </td><td> 66.1 </td><td> 70.6 </td></tr>
<tr><td>Mercedes</td><td>S</td><td>63 AMG</td><td>2008</td><td> 49.0 </td><td> 58.7 </td><td> 64.7 </td><td> 67.9 </td><td> 70.3 </td><td> 72.6 </td></tr>
<tr><td>Mercedes</td><td>S</td><td>400 Hybrid</td><td>2009</td><td> 43.0 </td><td> 52.9 </td><td> 60.8 </td><td> 64.5 </td><td> 66.1 </td><td> 68.1 </td></tr>
<tr><td>Mercedes</td><td>S</td><td>500 L 4 matic</td><td>2010</td><td> 40.2 </td><td> 55.8 </td><td> 59.3 </td><td> 62.9 </td><td> 64.9 </td><td> 66.9 </td></tr>
<tr><td>Mercedes</td><td>S</td><td>500</td><td>2013</td><td> 39.7 </td><td> 53.2 </td><td> 57.1 </td><td> 60.9 </td><td> 64.7 </td><td> 66.3 </td></tr>
<tr><td>Mercedes</td><td>S</td><td>500</td><td>2014</td><td> 37.9 </td><td> 48.8 </td><td> 55.6 </td><td> 59.4 </td><td> 61.6 </td><td> 63.9 </td></tr>
<tr><td>Mercedes</td><td>S</td><td>350d</td><td>2016</td><td> 43.0 </td><td> 53.6 </td><td> 56.8 </td><td> 60.2 </td><td> 63.3 </td><td> 66.2 </td></tr>
<tr><td>Mercedes</td><td>S</td><td>500e</td><td>2016</td><td> 37.9 </td><td> 49.8 </td><td> 54.0 </td><td> 58.2 </td><td> 60.4 </td><td> 63.5 </td></tr>
<tr><td>Mercedes</td><td>S</td><td>AMG S63</td><td>2016</td><td> 42.9 </td><td> 55.8 </td><td> 58.5 </td><td> 61.2 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Mercedes</td><td>SL</td><td>500</td><td>2012</td><td> 45.1 </td><td> 55.5 </td><td> 63.8 </td><td> 68.3 </td><td> 69.4 </td><td> 70.9 </td></tr>
<tr><td>Mercedes</td><td>SL</td><td>400</td><td>2016</td><td> 39.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Mercedes</td><td>SLK</td><td>350</td><td>2011</td><td> 46.7 </td><td> 57.5 </td><td> 66.1 </td><td> 70.2 </td><td> 71.9 </td><td> 74.0 </td></tr>
<tr><td>Mercedes</td><td>SLK</td><td>350</td><td>2012</td><td> 48.8 </td><td> 57.9 </td><td> 63.6 </td><td> 66.3 </td><td> 69.9 </td><td> 73.5 </td></tr>
<tr><td>Mercedes</td><td>SLS</td><td>AMG Roadster</td><td>2012</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 67.9 </td><td> 68.5 </td><td> 69.5 </td></tr>
<tr><td>Mercury</td><td>Grand Marquis</td><td>4.6 V8</td><td>2010</td><td> 44.4 </td><td> 55.8 </td><td> 62.8 </td><td> 66.8 </td><td> 69.0 </td><td> 71.2 </td></tr>
<tr><td>Mercury</td><td>Mariner</td><td>Hybrid</td><td>2008</td><td> 37.7 </td><td> 54.9 </td><td> 65.5 </td><td> 71.8 </td><td> 74.0 </td><td> 76.3 </td></tr>
<tr><td>Mini</td><td>Clubman</td><td>Cooper S</td><td>2012</td><td> 46.2 </td><td> 56.8 </td><td> 65.3 </td><td> 67.1 </td><td> 71.1 </td><td> 75.6 </td></tr>
<tr><td>Mini</td><td>Clubman</td><td>One</td><td>2016</td><td> 39.6 </td><td> 56.8 </td><td> 60.6 </td><td> 63.2 </td><td> 68.6 </td><td> 70.7 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>D</td><td>2008</td><td> 49.2 </td><td> 64.1 </td><td> 72.1 </td><td> 73.1 </td><td> 74.1 </td><td> 76.1 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>Cabrio</td><td>2009</td><td> 46.5 </td><td> 57.3 </td><td> 65.9 </td><td> 70.1 </td><td> 71.6 </td><td> 73.5 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>&nbsp;</td><td>2010</td><td> 41.4 </td><td> 62.7 </td><td> 65.8 </td><td> 68.4 </td><td> 71.1 </td><td> 73.4 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>Stationcar</td><td>2010</td><td> 37.0 </td><td> 59.6 </td><td> 64.1 </td><td> 67.4 </td><td> 70.1 </td><td> 73.1 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>1.6</td><td>2011</td><td> 46.3 </td><td> 56.6 </td><td> 63.1 </td><td> 66.2 </td><td> 69.7 </td><td> 73.2 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>S Coupe</td><td>2011</td><td> 45.8 </td><td> 56.4 </td><td> 64.9 </td><td> 69.1 </td><td> 70.5 </td><td> 72.3 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>Stationcar</td><td>2011</td><td> 37.2 </td><td> 60.2 </td><td> 65.1 </td><td> 67.0 </td><td> 70.8 </td><td> 73.1 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>&nbsp;</td><td>2014</td><td> 42.0 </td><td> 60.3 </td><td> 62.8 </td><td> 65.5 </td><td> 67.5 </td><td> 70.4 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>1.5</td><td>2014</td><td> 43.4 </td><td> 59.1 </td><td> 63.2 </td><td> 69.3 </td><td> 70.4 </td><td> 71.6 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>S Clubman</td><td>2015</td><td> 48.9 </td><td> 59.2 </td><td> 64.3 </td><td> 68.3 </td><td> 71.9 </td><td> 75.3 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>1.5 Cabrio</td><td>2016</td><td> 42.2 </td><td> 58.8 </td><td> 64.1 </td><td> 68.6 </td><td> 72.7 </td><td> 74.5 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>2.0D</td><td>2016</td><td> 45.1 </td><td> 59.2 </td><td> 61.7 </td><td> 64.3 </td><td> 67.3 </td><td> 70.7 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>Cabrio</td><td>2016</td><td> 45.9 </td><td> 65.7 </td><td> 68.5 </td><td> 70.1 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>S</td><td>2016</td><td> 40.9 </td><td> 61.8 </td><td> 65.0 </td><td> 68.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Mini</td><td>Cooper</td><td>S</td><td>2017</td><td> 38.9 </td><td> 61.8 </td><td> 65.5 </td><td> 69.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Mini</td><td>Countryman</td><td>Cooper</td><td>2012</td><td> 38.4 </td><td> 61.2 </td><td> 63.3 </td><td> 67.0 </td><td> 71.6 </td><td> 75.2 </td></tr>
<tr><td>Mini</td><td>Countryman</td><td>1.6</td><td>2014</td><td> 40.2 </td><td> 57.8 </td><td> 63.4 </td><td> 65.8 </td><td> 68.7 </td><td> 73.2 </td></tr>
<tr><td>Mini</td><td>Countryman</td><td>&nbsp;</td><td>2015</td><td> 43.6 </td><td> 60.2 </td><td> 63.6 </td><td> 66.9 </td><td> 69.6 </td><td> 71.3 </td></tr>
<tr><td>Mini</td><td>Countryman</td><td>1.6</td><td>2015</td><td> 39.3 </td><td> 59.0 </td><td> 63.8 </td><td> 66.3 </td><td> 69.9 </td><td> 73.0 </td></tr>
<tr><td>Mini</td><td>Roadster</td><td>Cooper S</td><td>2012</td><td> 44.8 </td><td> 55.1 </td><td> 63.4 </td><td> 67.6 </td><td> 68.9 </td><td> 70.6 </td></tr>
<tr><td>Mitsubihi</td><td>Lancer</td><td>Sportback 1.6</td><td>2011</td><td> 45.0 </td><td> 55.4 </td><td> 63.8 </td><td> 68.9 </td><td> 69.3 </td><td> 70.1 </td></tr>
<tr><td>Mitsubishi</td><td>ASX</td><td>1.6</td><td>2010</td><td> 43.8 </td><td> 53.9 </td><td> 62.0 </td><td> 66.9 </td><td> 67.4 </td><td> 68.2 </td></tr>
<tr><td>Mitsubishi</td><td>ASX</td><td>1.6</td><td>2013</td><td> 44.1 </td><td> 59.0 </td><td> 62.5 </td><td> 65.0 </td><td> 68.9 </td><td> 72.2 </td></tr>
<tr><td>Mitsubishi</td><td>ASX</td><td>1.6</td><td>2015</td><td> 44.9 </td><td> 61.2 </td><td> 65.1 </td><td> 68.9 </td><td> 72.5 </td><td> 74.3 </td></tr>
<tr><td>Mitsubishi</td><td>ASX</td><td>1.6</td><td>2016</td><td> 40.2 </td><td> 59.7 </td><td> 64.6 </td><td> 69.2 </td><td> 72.7 </td><td> 76.1 </td></tr>
<tr><td>Mitsubishi</td><td>Colt</td><td>1.3 Invit</td><td>2009</td><td> 42.2 </td><td> 61.8 </td><td> 66.3 </td><td> 69.6 </td><td> 72.1 </td><td> 75.1 </td></tr>
<tr><td>Mitsubishi</td><td>Colt</td><td>1.3</td><td>2010</td><td> 41.7 </td><td> 60.8 </td><td> 64.8 </td><td> 67.7 </td><td> 70.6 </td><td> 73.3 </td></tr>
<tr><td>Mitsubishi</td><td>i</td><td>0.7</td><td>2010</td><td> 47.3 </td><td> 56.2 </td><td> 61.6 </td><td> 64.9 </td><td> 65.8 </td><td> 66.6 </td></tr>
<tr><td>Mitsubishi</td><td>Lancer</td><td>110</td><td>2008</td><td> 39.2 </td><td> 63.3 </td><td> 69.2 </td><td> 70.6 </td><td> 74.6 </td><td> 75.1 </td></tr>
<tr><td>Mitsubishi</td><td>Lancer</td><td>Evo X</td><td>2008</td><td> 45.6 </td><td> 58.2 </td><td> 65.9 </td><td> 70.4 </td><td> 72.4 </td><td> 74.5 </td></tr>
<tr><td>Mitsubishi</td><td>Lancer</td><td>Evolution MR</td><td>2008</td><td> 46.5 </td><td> 57.2 </td><td> 65.8 </td><td> 70.1 </td><td> 71.5 </td><td> 73.3 </td></tr>
<tr><td>Mitsubishi</td><td>Lancer</td><td>GTS</td><td>2008</td><td> 43.9 </td><td> 55.3 </td><td> 62.4 </td><td> 66.1 </td><td> 69.5 </td><td> 72.9 </td></tr>
<tr><td>Mitsubishi</td><td>Lancer</td><td>1.8 Stationcar</td><td>2009</td><td> 47.3 </td><td> 58.2 </td><td> 67.0 </td><td> 69.4 </td><td> 72.9 </td><td> 76.9 </td></tr>
<tr><td>Mitsubishi</td><td>Lancer </td><td>2.0 DI-D</td><td>2008</td><td> 46.2 </td><td> 56.8 </td><td> 65.3 </td><td> 69.7 </td><td> 71.0 </td><td> 72.7 </td></tr>
<tr><td>Mitsubishi</td><td>Outlander</td><td>2.2 DI-D</td><td>2008</td><td> 45.5 </td><td> 62.1 </td><td> 64.4 </td><td> 67.5 </td><td> 71.3 </td><td> 72.8 </td></tr>
<tr><td>Mitsubishi</td><td>Outlander</td><td>2.4 CVT</td><td>2008</td><td> 41.2 </td><td> 61.6 </td><td> 66.1 </td><td> 68.1 </td><td> 72.1 </td><td> 74.4 </td></tr>
<tr><td>Mitsubishi</td><td>Outlander</td><td>2.2 DI-D</td><td>2010</td><td> 43.4 </td><td> 53.4 </td><td> 61.4 </td><td> 64.0 </td><td> 66.8 </td><td> 70.0 </td></tr>
<tr><td>Mitsubishi</td><td>Outlander</td><td>2.0</td><td>2011</td><td> 39.1 </td><td> 53.9 </td><td> 63.1 </td><td> 68.3 </td><td> 71.0 </td><td> 73.8 </td></tr>
<tr><td>Mitsubishi</td><td>Outlander</td><td>2.0</td><td>2013</td><td> 45.8 </td><td> 59.6 </td><td> 65.1 </td><td> 69.6 </td><td> 71.8 </td><td> 76.0 </td></tr>
<tr><td>Mitsubishi</td><td>Outlander</td><td>PHEV</td><td>2014</td><td> 44.0 </td><td> 55.6 </td><td> 59.6 </td><td> 64.6 </td><td> 67.8 </td><td> 70.2 </td></tr>
<tr><td>Mitsubishi</td><td>Space Star</td><td>1.0</td><td>2013</td><td> 48.2 </td><td> 60.1 </td><td> 66.5 </td><td> 69.3 </td><td> 74.2 </td><td> 77.4 </td></tr>
<tr><td>Mitsubishi</td><td>Space Star</td><td>1.0</td><td>2013</td><td> 42.4 </td><td> 59.6 </td><td> 65.5 </td><td> 69.1 </td><td> 72.5 </td><td> 75.0 </td></tr>
<tr><td>Mitsubishi</td><td>Space Star</td><td>1.2</td><td>2017</td><td> 43.5 </td><td> 59.3 </td><td> 65.0 </td><td> 68.2 </td><td> 74.6 </td><td> 74.7 </td></tr>
<tr><td>Nissan</td><td>350Z</td><td>&nbsp;</td><td>2008</td><td> 46.3 </td><td> 57.0 </td><td> 65.5 </td><td> 69.7 </td><td> 71.2 </td><td> 73.1 </td></tr>
<tr><td>Nissan</td><td>370Z</td><td>&nbsp;</td><td>2009</td><td> 48.0 </td><td> 59.2 </td><td> 66.3 </td><td> 69.8 </td><td> 73.4 </td><td> 77.1 </td></tr>
<tr><td>Nissan</td><td>370Z</td><td>&nbsp;</td><td>2010</td><td> 47.3 </td><td> 58.2 </td><td> 67.0 </td><td> 70.5 </td><td> 72.9 </td><td> 75.6 </td></tr>
<tr><td>Nissan</td><td>370Z</td><td>Cabrio</td><td>2010</td><td> 48.1 </td><td> 58.6 </td><td> 65.2 </td><td> 68.5 </td><td> 71.8 </td><td> 75.2 </td></tr>
<tr><td>Nissan</td><td>370Z</td><td>&nbsp;</td><td>2017</td><td> 44.9 </td><td> 65.7 </td><td> 68.5 </td><td> 71.3 </td><td> 74.0 </td><td> 77.8 </td></tr>
<tr><td>Nissan</td><td>Altima</td><td>3.5 V6</td><td>2008</td><td> 39.3 </td><td> 51.8 </td><td> 59.7 </td><td> 63.8 </td><td> 67.1 </td><td> 70.5 </td></tr>
<tr><td>Nissan</td><td>Altima</td><td>3.5 V6</td><td>2012</td><td> 38.7 </td><td> 49.4 </td><td> 56.1 </td><td> 59.4 </td><td> 63.0 </td><td> 66.5 </td></tr>
<tr><td>Nissan</td><td>Altima</td><td>2.5</td><td>2013</td><td> 39.7 </td><td> 50.8 </td><td> 57.6 </td><td> 61.4 </td><td> 63.9 </td><td> 66.5 </td></tr>
<tr><td>Nissan</td><td>Altima</td><td>2.5</td><td>2016</td><td> 41.9 </td><td> 52.3 </td><td> 58.7 </td><td> 62.3 </td><td> 64.4 </td><td> 66.5 </td></tr>
<tr><td>Nissan</td><td>Cube</td><td>S</td><td>2009</td><td> 41.0 </td><td> 55.9 </td><td> 65.0 </td><td> 70.7 </td><td> 71.7 </td><td> 72.7 </td></tr>
<tr><td>Nissan</td><td>Cube</td><td>1.6 CVT</td><td>2010</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 66.5 </td><td> 68.3 </td><td> 70.5 </td></tr>
<tr><td>Nissan</td><td>GT-R</td><td>&nbsp;</td><td>2009</td><td> 52.6 </td><td> 64.9 </td><td> 72.5 </td><td> 76.9 </td><td> 79.0 </td><td> 81.2 </td></tr>
<tr><td>Nissan</td><td>GT-R</td><td>&nbsp;</td><td>2011</td><td> 51.9 </td><td> 65.8 </td><td> 67.4 </td><td> 72.1 </td><td> 74.5 </td><td> 75.3 </td></tr>
<tr><td>Nissan</td><td>GT-R</td><td>&nbsp;</td><td>2012</td><td> 51.5 </td><td> 61.2 </td><td> 67.2 </td><td> 70.3 </td><td> 73.4 </td><td> 76.5 </td></tr>
<tr><td>Nissan</td><td>GT-R</td><td>&nbsp;</td><td>2013</td><td> 50.9 </td><td> 62.8 </td><td> 70.1 </td><td> 74.2 </td><td> 76.7 </td><td> 79.2 </td></tr>
<tr><td>Nissan</td><td>GT-R</td><td>3.8 V6</td><td>2017</td><td> 48.9 </td><td> 64.7 </td><td> 68.0 </td><td> 71.3 </td><td> 72.1 </td><td> 75.8 </td></tr>
<tr><td>Nissan</td><td>Juke</td><td>1.6</td><td>2011</td><td> 42.5 </td><td> 56.6 </td><td> 65.2 </td><td> 70.3 </td><td> 72.0 </td><td> 73.8 </td></tr>
<tr><td>Nissan</td><td>Juke</td><td>1.6 DIG-T</td><td>2011</td><td> 37.9 </td><td> 59.8 </td><td> 66.2 </td><td> 68.8 </td><td> 70.2 </td><td> 72.7 </td></tr>
<tr><td>Nissan</td><td>Juke</td><td>1.6</td><td>2013</td><td> 38.0 </td><td> 57.6 </td><td> 64.1 </td><td> 66.3 </td><td> 70.3 </td><td> 73.6 </td></tr>
<tr><td>Nissan</td><td>Juke</td><td>Nismo</td><td>2013</td><td> 40.8 </td><td> 54.3 </td><td> 62.5 </td><td> 67.7 </td><td> 68.7 </td><td> 69.8 </td></tr>
<tr><td>Nissan</td><td>Juke</td><td>1.2</td><td>2014</td><td> 41.4 </td><td> 56.9 </td><td> 62.4 </td><td> 65.1 </td><td> 68.8 </td><td> 71.7 </td></tr>
<tr><td>Nissan</td><td>Leaf</td><td>&nbsp;</td><td>2011</td><td> 37.2 </td><td> 53.2 </td><td> 63.1 </td><td> 68.7 </td><td> 71.8 </td><td> 74.9 </td></tr>
<tr><td>Nissan</td><td>Leaf</td><td>&nbsp;</td><td>2011</td><td> 42.8 </td><td> 52.7 </td><td> 60.6 </td><td> 64.7 </td><td> 65.9 </td><td> 67.5 </td></tr>
<tr><td>Nissan</td><td>Leaf</td><td>&nbsp;</td><td>2013</td><td> 44.9 </td><td> 58.5 </td><td> 62.3 </td><td> 66.3 </td><td> 69.1 </td><td> 70.7 </td></tr>
<tr><td>Nissan</td><td>Leaf</td><td>EV</td><td>2017</td><td> 44.1 </td><td> 54.3 </td><td> 59.7 </td><td> 61.8 </td><td> 68.0 </td><td> 68.1 </td></tr>
<tr><td>Nissan</td><td>Maxima</td><td>3.5 V6</td><td>2009</td><td> 42.5 </td><td> 55.8 </td><td> 63.9 </td><td> 68.9 </td><td> 70.1 </td><td> 71.3 </td></tr>
<tr><td>Nissan</td><td>Micra</td><td>1.2</td><td>2011</td><td> 48.1 </td><td> 62.1 </td><td> 66.6 </td><td> 71.5 </td><td> 74.1 </td><td> 75.2 </td></tr>
<tr><td>Nissan</td><td>Micra</td><td>1.2</td><td>2011</td><td> 43.4 </td><td> 53.4 </td><td> 61.5 </td><td> 65.4 </td><td> 66.8 </td><td> 68.6 </td></tr>
<tr><td>Nissan</td><td>Micra</td><td>1.2</td><td>2012</td><td> 45.5 </td><td> 56.0 </td><td> 64.4 </td><td> 68.2 </td><td> 70.0 </td><td> 72.2 </td></tr>
<tr><td>Nissan</td><td>Micra</td><td>0.9</td><td>2017</td><td> 46.7 </td><td> 56.7 </td><td> 62.2 </td><td> 65.3 </td><td> 71.9 </td><td> 72.0 </td></tr>
<tr><td>Nissan</td><td>Micra</td><td>0.9</td><td>2017</td><td> 41.3 </td><td> 57.4 </td><td> 62.2 </td><td> 65.8 </td><td> 71.4 </td><td> 71.5 </td></tr>
<tr><td>Nissan</td><td>Micra</td><td>0.9</td><td>2017</td><td> 40.9 </td><td> 59.8 </td><td> 63.0 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Nissan</td><td>Murano</td><td>3.5 V6</td><td>2008</td><td> 40.8 </td><td> 50.2 </td><td> 57.8 </td><td> 61.9 </td><td> 62.8 </td><td> 64.0 </td></tr>
<tr><td>Nissan</td><td>Murano</td><td>3.5 V6</td><td>2009</td><td> 41.6 </td><td> 54.1 </td><td> 61.8 </td><td> 66.1 </td><td> 68.5 </td><td> 70.9 </td></tr>
<tr><td>Nissan</td><td>Murano</td><td>CrossCabriolet</td><td>2011</td><td> 44.0 </td><td> 56.0 </td><td> 63.4 </td><td> 67.7 </td><td> 69.5 </td><td> 71.3 </td></tr>
<tr><td>Nissan</td><td>Navara</td><td>2.5 DCI</td><td>2012</td><td> 47.2 </td><td> 62.2 </td><td> 66.1 </td><td> 67.4 </td><td> 70.3 </td><td> 73.2 </td></tr>
<tr><td>Nissan</td><td>Note</td><td>1.4</td><td>2009</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 65.5 </td><td> 68.3 </td><td> 71.5 </td></tr>
<tr><td>Nissan</td><td>Note</td><td>1.4 L</td><td>2010</td><td> 40.0 </td><td> 61.1 </td><td> 66.6 </td><td> 68.6 </td><td> 73.6 </td><td> 74.6 </td></tr>
<tr><td>Nissan</td><td>Note</td><td>1.2</td><td>2014</td><td> 41.2 </td><td> 61.2 </td><td> 65.4 </td><td> 67.8 </td><td> 71.3 </td><td> 74.3 </td></tr>
<tr><td>Nissan</td><td>Note</td><td>1.2</td><td>2016</td><td> 39.6 </td><td> 56.3 </td><td> 62.3 </td><td> 65.7 </td><td> 69.4 </td><td> 72.8 </td></tr>
<tr><td>Nissan</td><td>Pathfinder</td><td>5.6 V8</td><td>2008</td><td> 43.1 </td><td> 54.9 </td><td> 62.0 </td><td> 66.4 </td><td> 67.7 </td><td> 69.0 </td></tr>
<tr><td>Nissan</td><td>Pathfinder</td><td>3.5 V6</td><td>2012</td><td> 39.9 </td><td> 51.1 </td><td> 58.1 </td><td> 61.8 </td><td> 64.7 </td><td> 67.6 </td></tr>
<tr><td>Nissan</td><td>Pixo</td><td>1.0</td><td>2009</td><td> 40.9 </td><td> 63.8 </td><td> 67.0 </td><td> 70.5 </td><td> 73.0 </td><td> 76.9 </td></tr>
<tr><td>Nissan</td><td>Pulsar</td><td>1.2</td><td>2014</td><td> 43.3 </td><td> 56.9 </td><td> 60.1 </td><td> 62.7 </td><td> 66.6 </td><td> 69.0 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>1.6</td><td>2008</td><td> 44.7 </td><td> 55.0 </td><td> 63.3 </td><td> 66.8 </td><td> 68.9 </td><td> 71.2 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>2.0 dCI</td><td>2008</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 66.8 </td><td> 68.3 </td><td> 70.2 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>2.0</td><td>2009</td><td> 36.6 </td><td> 57.0 </td><td> 63.9 </td><td> 66.3 </td><td> 70.1 </td><td> 72.9 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>1.6</td><td>2010</td><td> 41.2 </td><td> 58.1 </td><td> 65.1 </td><td> 67.1 </td><td> 70.1 </td><td> 75.1 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>1.6</td><td>2012</td><td> 40.2 </td><td> 56.4 </td><td> 62.2 </td><td> 67.6 </td><td> 70.1 </td><td> 73.9 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>1.6</td><td>2012</td><td> 45.3 </td><td> 55.8 </td><td> 64.1 </td><td> 68.6 </td><td> 69.7 </td><td> 71.2 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>1.2</td><td>2014</td><td> 36.8 </td><td> 55.9 </td><td> 59.7 </td><td> 63.6 </td><td> 65.7 </td><td> 69.7 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>1.6</td><td>2015</td><td> 44.3 </td><td> 57.2 </td><td> 62.3 </td><td> 65.4 </td><td> 68.2 </td><td> 71.3 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>1.2</td><td>2016</td><td> 38.1 </td><td> 55.2 </td><td> 60.2 </td><td> 63.0 </td><td> 67.9 </td><td> 70.0 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>1.2</td><td>2017</td><td> 39.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>1.6</td><td>2017</td><td> 42.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Nissan</td><td>Qashqai</td><td>1.6D</td><td>2017</td><td> 47.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Nissan</td><td>Qashqai+2</td><td>2.0</td><td>2009</td><td> 44.1 </td><td> 54.3 </td><td> 62.5 </td><td> 64.9 </td><td> 68.0 </td><td> 71.5 </td></tr>
<tr><td>Nissan</td><td>Rogue</td><td>2.5</td><td>2008</td><td> 42.9 </td><td> 56.6 </td><td> 65.1 </td><td> 69.8 </td><td> 72.8 </td><td> 75.9 </td></tr>
<tr><td>Nissan</td><td>Rogue</td><td>2.5</td><td>2014</td><td> 39.5 </td><td> 51.8 </td><td> 59.4 </td><td> 63.8 </td><td> 66.0 </td><td> 68.2 </td></tr>
<tr><td>Nissan</td><td>Rogue</td><td>2.5</td><td>2016</td><td> 43.2 </td><td> 53.4 </td><td> 59.8 </td><td> 63.3 </td><td> 65.4 </td><td> 67.5 </td></tr>
<tr><td>Nissan</td><td>Titan</td><td>5.6 V8</td><td>2016</td><td> 43.7 </td><td> 56.0 </td><td> 63.5 </td><td> 68.1 </td><td> 69.3 </td><td> 70.5 </td></tr>
<tr><td>Nissan</td><td>Versa</td><td>1.6</td><td>2012</td><td> 43.5 </td><td> 56.0 </td><td> 63.7 </td><td> 68.1 </td><td> 70.4 </td><td> 72.7 </td></tr>
<tr><td>Nissan</td><td>X-Trail</td><td>2.0 dCI</td><td>2008</td><td> 45.1 </td><td> 55.5 </td><td> 63.8 </td><td> 67.5 </td><td> 69.4 </td><td> 71.7 </td></tr>
<tr><td>Nissan</td><td>X-trail</td><td>1.6D</td><td>2015</td><td> 44.4 </td><td> 60.9 </td><td> 63.2 </td><td> 66.0 </td><td> 69.1 </td><td> 71.4 </td></tr>
<tr><td>Nissan</td><td>X-Trail</td><td>1.6</td><td>2017</td><td> 38.0 </td><td> 55.5 </td><td> 61.6 </td><td> 65.0 </td><td> 72.0 </td><td> 72.1 </td></tr>
<tr><td>Opel</td><td>Agila</td><td>1.0</td><td>2008</td><td> 47.4 </td><td> 58.3 </td><td> 67.1 </td><td> 71.1 </td><td> 72.9 </td><td> 75.1 </td></tr>
<tr><td>Opel</td><td>Agila</td><td>1.0</td><td>2013</td><td> 37.6 </td><td> 59.9 </td><td> 65.5 </td><td> 68.3 </td><td> 71.7 </td><td> 74.2 </td></tr>
<tr><td>Opel</td><td>Agile</td><td>1.0</td><td>2011</td><td> 47.4 </td><td> 58.3 </td><td> 67.1 </td><td> 71.1 </td><td> 72.9 </td><td> 75.1 </td></tr>
<tr><td>Opel</td><td>Ampera</td><td>1.4 Hybrid</td><td>2012</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 67.0 </td><td> 68.0 </td><td> 69.4 </td></tr>
<tr><td>Opel</td><td>Ampera-e</td><td>EV</td><td>2017</td><td> 45.2 </td><td> 54.1 </td><td> 60.5 </td><td> 63.7 </td><td> 69.7 </td><td> 69.8 </td></tr>
<tr><td>Opel</td><td>Antara</td><td>2.0 CDTI</td><td>2008</td><td> 45.3 </td><td> 55.8 </td><td> 64.1 </td><td> 68.7 </td><td> 69.7 </td><td> 71.1 </td></tr>
<tr><td>Opel</td><td>Antera</td><td>2.4</td><td>2011</td><td> 44.1 </td><td> 54.2 </td><td> 62.4 </td><td> 66.2 </td><td> 67.8 </td><td> 69.8 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.6 GTC</td><td>2008</td><td> 45.6 </td><td> 56.1 </td><td> 64.5 </td><td> 67.8 </td><td> 70.2 </td><td> 72.8 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.6 turbo</td><td>2008</td><td> 45.1 </td><td> 55.5 </td><td> 63.8 </td><td> 67.0 </td><td> 69.5 </td><td> 72.2 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>GTC 1.6</td><td>2008</td><td> 44.5 </td><td> 61.8 </td><td> 65.7 </td><td> 68.6 </td><td> 70.4 </td><td> 74.4 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.4 Turbo</td><td>2009</td><td> 45.3 </td><td> 59.1 </td><td> 63.2 </td><td> 65.7 </td><td> 66.8 </td><td> 69.5 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.4 Turbo</td><td>2010</td><td> 38.9 </td><td> 59.7 </td><td> 63.5 </td><td> 66.5 </td><td> 69.2 </td><td> 71.6 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.6 Turbo</td><td>2010</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 68.2 </td><td> 69.0 </td><td> 70.2 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.6 Twintop</td><td>2010</td><td> 42.1 </td><td> 60.6 </td><td> 65.5 </td><td> 68.6 </td><td> 70.9 </td><td> 73.4 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.6 Turbo</td><td>2011</td><td> 44.9 </td><td> 57.1 </td><td> 62.3 </td><td> 66.4 </td><td> 69.1 </td><td> 72.1 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.6 Turbo Stationcar</td><td>2011</td><td> 39.9 </td><td> 59.3 </td><td> 64.4 </td><td> 66.7 </td><td> 69.5 </td><td> 72.1 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.4</td><td>2012</td><td> 44.9 </td><td> 60.1 </td><td> 64.5 </td><td> 67.5 </td><td> 69.0 </td><td> 73.9 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.4 turbo</td><td>2012</td><td> 41.6 </td><td> 57.8 </td><td> 61.8 </td><td> 65.5 </td><td> 68.8 </td><td> 70.2 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.6 Stationcar</td><td>2012</td><td> 43.7 </td><td> 53.8 </td><td> 61.9 </td><td> 65.1 </td><td> 67.4 </td><td> 69.9 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>GTC</td><td>2012</td><td> 46.3 </td><td> 60.8 </td><td> 65.8 </td><td> 68.3 </td><td> 71.4 </td><td> 73.0 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>GTC 1.6</td><td>2012</td><td> 45.3 </td><td> 55.8 </td><td> 64.1 </td><td> 67.3 </td><td> 69.8 </td><td> 72.7 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.4</td><td>2015</td><td> 38.2 </td><td> 57.1 </td><td> 61.1 </td><td> 64.6 </td><td> 69.1 </td><td> 70.1 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.0</td><td>2016</td><td> 40.9 </td><td> 58.8 </td><td> 62.0 </td><td> 65.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.6D</td><td>2016</td><td> 47.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.6D Estate</td><td>2016</td><td> 42.3 </td><td> 55.5 </td><td> 61.1 </td><td> 64.5 </td><td> 66.8 </td><td> 70.9 </td></tr>
<tr><td>Opel</td><td>Astra</td><td>1.0</td><td>2017</td><td> 37.9 </td><td> 56.8 </td><td> 61.5 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Opel</td><td>Cascada</td><td>1.6</td><td>2014</td><td> 38.5 </td><td> 55.9 </td><td> 61.4 </td><td> 64.8 </td><td> 68.2 </td><td> 71.4 </td></tr>
<tr><td>Opel</td><td>Corsa</td><td>1.6 Turbo GSI</td><td>2008</td><td> 46.7 </td><td> 57.5 </td><td> 66.1 </td><td> 67.7 </td><td> 72.0 </td><td> 76.9 </td></tr>
<tr><td>Opel</td><td>Corsa</td><td>1.2</td><td>2009</td><td> 45.2 </td><td> 55.6 </td><td> 63.9 </td><td> 67.3 </td><td> 69.6 </td><td> 72.1 </td></tr>
<tr><td>Opel</td><td>Corsa</td><td>1.4</td><td>2010</td><td> 39.9 </td><td> 60.2 </td><td> 65.2 </td><td> 66.3 </td><td> 69.7 </td><td> 71.4 </td></tr>
<tr><td>Opel</td><td>Corsa</td><td>1.2</td><td>2011</td><td> 45.4 </td><td> 55.9 </td><td> 64.3 </td><td> 67.4 </td><td> 70.0 </td><td> 73.0 </td></tr>
<tr><td>Opel</td><td>Corsa</td><td>1.3 CDTI</td><td>2011</td><td> 46.3 </td><td> 62.7 </td><td> 65.8 </td><td> 68.0 </td><td> 71.2 </td><td> 74.5 </td></tr>
<tr><td>Opel</td><td>Corsa</td><td>1.3 CDTI</td><td>2012</td><td> 46.3 </td><td> 57.0 </td><td> 65.6 </td><td> 68.6 </td><td> 71.4 </td><td> 74.6 </td></tr>
<tr><td>Opel</td><td>Corsa</td><td>1.0</td><td>2015</td><td> 45.8 </td><td> 58.2 </td><td> 62.6 </td><td> 66.5 </td><td> 70.5 </td><td> 72.9 </td></tr>
<tr><td>Opel</td><td>Corsa</td><td>1.0</td><td>2016</td><td> 41.1 </td><td> 61.2 </td><td> 64.8 </td><td> 68.3 </td><td> 69.2 </td><td> 72.8 </td></tr>
<tr><td>Opel</td><td>Corsa</td><td>OPC</td><td>2016</td><td> 45.9 </td><td> 63.7 </td><td> 66.5 </td><td> 69.3 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>Opel</td><td>Corsa</td><td>1.0</td><td>2017</td><td> 45.9 </td><td> 60.8 </td><td> 64.0 </td><td> 67.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Opel</td><td>Crossland X</td><td>1.2</td><td>2017</td><td> 40.3 </td><td> 56.3 </td><td> 60.9 </td><td> 63.2 </td><td> 71.2 </td><td> 71.3 </td></tr>
<tr><td>Opel</td><td>Insignia</td><td>1.6 Turbo Stationcar</td><td>2009</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 65.7 </td><td> 68.3 </td><td> 71.3 </td></tr>
<tr><td>Opel</td><td>Insignia</td><td>2.0 T 4x4</td><td>2009</td><td> 45.1 </td><td> 62.0 </td><td> 66.0 </td><td> 69.0 </td><td> 70.2 </td><td> 72.0 </td></tr>
<tr><td>Opel</td><td>Insignia</td><td>1.4</td><td>2012</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 68.0 </td><td> 68.7 </td><td> 69.8 </td></tr>
<tr><td>Opel</td><td>Insignia</td><td>2.0 CDTI</td><td>2012</td><td> 43.7 </td><td> 53.8 </td><td> 61.8 </td><td> 66.1 </td><td> 67.2 </td><td> 68.7 </td></tr>
<tr><td>Opel</td><td>Insignia</td><td>1.6</td><td>2014</td><td> 38.1 </td><td> 58.2 </td><td> 62.2 </td><td> 66.3 </td><td> 68.3 </td><td> 71.8 </td></tr>
<tr><td>Opel</td><td>Insignia</td><td>2.0D</td><td>2015</td><td> 46.5 </td><td> 58.9 </td><td> 62.7 </td><td> 66.6 </td><td> 68.8 </td><td> 71.7 </td></tr>
<tr><td>Opel</td><td>Insignia</td><td>2.0D</td><td>2016</td><td> 47.9 </td><td> 57.8 </td><td> 62.0 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Opel</td><td>Insignia</td><td>2.0d</td><td>2017</td><td> 44.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Opel</td><td>Insignia</td><td>2.0d stationcar</td><td>2017</td><td> 45.3 </td><td> 57.0 </td><td> 61.2 </td><td> 63.9 </td><td> 70.1 </td><td> 70.2 </td></tr>
<tr><td>Opel</td><td>Insignia </td><td>1.5</td><td>2017</td><td> 45.2 </td><td> 55.6 </td><td> 60.1 </td><td> 63.4 </td><td> 69.6 </td><td> 69.7 </td></tr>
<tr><td>Opel</td><td>Karl</td><td>1.0</td><td>2017</td><td> 39.9 </td><td> 59.8 </td><td> 63.0 </td><td> 66.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Opel</td><td>Meriva</td><td>1.4 Turbo</td><td>2010</td><td> 43.3 </td><td> 59.2 </td><td> 64.9 </td><td> 66.5 </td><td> 69.3 </td><td> 72.0 </td></tr>
<tr><td>Opel</td><td>Meriva</td><td>1.4 turbo</td><td>2012</td><td> 46.3 </td><td> 57.9 </td><td> 64.0 </td><td> 68.4 </td><td> 71.4 </td><td> 73.6 </td></tr>
<tr><td>Opel</td><td>Mokka</td><td>1.6</td><td>2013</td><td> 38.0 </td><td> 59.8 </td><td> 66.0 </td><td> 67.6 </td><td> 69.6 </td><td> 73.6 </td></tr>
<tr><td>Opel</td><td>Mokka</td><td>1.4</td><td>2014</td><td> 41.5 </td><td> 57.5 </td><td> 61.6 </td><td> 65.4 </td><td> 68.4 </td><td> 71.8 </td></tr>
<tr><td>Opel</td><td>Mokka</td><td>1.6D</td><td>2017</td><td> 46.9 </td><td> 61.8 </td><td> 64.5 </td><td> 67.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Opel</td><td>Zafira</td><td>1.7 CDTI</td><td>2008</td><td> 47.5 </td><td> 58.8 </td><td> 63.2 </td><td> 68.7 </td><td> 71.3 </td><td> 73.0 </td></tr>
<tr><td>Opel</td><td>Zafira</td><td>1.6 Turbo</td><td>2010</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 66.4 </td><td> 68.3 </td><td> 70.6 </td></tr>
<tr><td>Opel</td><td>Zafira</td><td>1.4</td><td>2012</td><td> 44.5 </td><td> 57.2 </td><td> 61.6 </td><td> 64.9 </td><td> 68.6 </td><td> 72.3 </td></tr>
<tr><td>Opel</td><td>Zafira</td><td>1.4</td><td>2012</td><td> 44.6 </td><td> 54.9 </td><td> 63.1 </td><td> 66.1 </td><td> 68.7 </td><td> 71.7 </td></tr>
<tr><td>Opel</td><td>Zafira</td><td>1.6D</td><td>2015</td><td> 43.6 </td><td> 59.2 </td><td> 63.1 </td><td> 66.9 </td><td> 69.6 </td><td> 71.3 </td></tr>
<tr><td>Opel</td><td>Zafira</td><td>2.0D Tourer</td><td>2015</td><td> 42.9 </td><td> 58.2 </td><td> 62.1 </td><td> 65.9 </td><td> 69.6 </td><td> 71.3 </td></tr>
<tr><td>Opel</td><td>Zafira Tourer</td><td>2.0D </td><td>2016</td><td> 44.1 </td><td> 59.2 </td><td> 63.3 </td><td> 67.3 </td><td> 68.3 </td><td> 71.8 </td></tr>
<tr><td>Peugeot</td><td>107</td><td>1.0</td><td>2008</td><td> 47.5 </td><td> 58.4 </td><td> 67.2 </td><td> 69.7 </td><td> 73.1 </td><td> 76.9 </td></tr>
<tr><td>Peugeot</td><td>107</td><td>1.0</td><td>2011</td><td> 46.7 </td><td> 57.5 </td><td> 66.1 </td><td> 70.0 </td><td> 71.9 </td><td> 74.2 </td></tr>
<tr><td>Peugeot</td><td>107</td><td>1.0</td><td>2012</td><td> 47.7 </td><td> 64.3 </td><td> 68.0 </td><td> 70.3 </td><td> 73.4 </td><td> 76.6 </td></tr>
<tr><td>Peugeot</td><td>107</td><td>1.0</td><td>2013</td><td> 41.3 </td><td> 64.2 </td><td> 66.8 </td><td> 69.9 </td><td> 74.0 </td><td> 75.9 </td></tr>
<tr><td>Peugeot</td><td>206</td><td>1.4 XS</td><td>2010</td><td> 45.4 </td><td> 65.2 </td><td> 69.6 </td><td> 70.9 </td><td> 73.9 </td><td> 76.8 </td></tr>
<tr><td>Peugeot</td><td>206</td><td>1.4</td><td>2011</td><td> 47.0 </td><td> 57.8 </td><td> 66.5 </td><td> 70.4 </td><td> 72.3 </td><td> 74.6 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>1.4</td><td>2008</td><td> 46.8 </td><td> 57.6 </td><td> 66.2 </td><td> 69.7 </td><td> 72.1 </td><td> 74.7 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>1.4 Stationcar</td><td>2008</td><td> 42.2 </td><td> 59.6 </td><td> 64.1 </td><td> 67.1 </td><td> 70.1 </td><td> 73.3 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>1.6 16V HDIF</td><td>2008</td><td> 44.5 </td><td> 62.5 </td><td> 65.4 </td><td> 68.5 </td><td> 70.4 </td><td> 74.5 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>1.6 HDiF Stationcar</td><td>2008</td><td> 45.3 </td><td> 55.8 </td><td> 64.1 </td><td> 67.5 </td><td> 69.8 </td><td> 72.3 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>1.6 Stationcar</td><td>2008</td><td> 46.3 </td><td> 57.0 </td><td> 65.5 </td><td> 69.2 </td><td> 71.3 </td><td> 73.6 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>RC Stationcar</td><td>2008</td><td> 44.6 </td><td> 64.0 </td><td> 67.0 </td><td> 69.0 </td><td> 71.5 </td><td> 74.3 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>1.4 Stationcar</td><td>2009</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 65.8 </td><td> 68.3 </td><td> 71.0 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>1.4 VTi</td><td>2010</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 65.8 </td><td> 68.3 </td><td> 71.0 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>1.6 THP</td><td>2010</td><td> 44.9 </td><td> 55.3 </td><td> 63.6 </td><td> 67.6 </td><td> 69.1 </td><td> 71.0 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>1.6 THP CC</td><td>2010</td><td> 45.4 </td><td> 55.8 </td><td> 64.2 </td><td> 67.9 </td><td> 69.8 </td><td> 72.1 </td></tr>
<tr><td>Peugeot</td><td>207</td><td>1.6 VTI 16v XS</td><td>2010</td><td> 37.7 </td><td> 59.6 </td><td> 63.4 </td><td> 66.5 </td><td> 70.0 </td><td> 74.2 </td></tr>
<tr><td>Peugeot</td><td>208</td><td>1.2 VTI</td><td>2012</td><td> 45.0 </td><td> 58.8 </td><td> 63.3 </td><td> 65.2 </td><td> 69.3 </td><td> 71.9 </td></tr>
<tr><td>Peugeot</td><td>208</td><td>1.4</td><td>2012</td><td> 44.9 </td><td> 55.3 </td><td> 63.6 </td><td> 66.1 </td><td> 69.2 </td><td> 72.7 </td></tr>
<tr><td>Peugeot</td><td>208</td><td>1.6 VTI</td><td>2012</td><td> 41.0 </td><td> 57.9 </td><td> 60.8 </td><td> 64.3 </td><td> 68.3 </td><td> 71.4 </td></tr>
<tr><td>Peugeot</td><td>208</td><td>GTI</td><td>2016</td><td> 43.9 </td><td> 62.7 </td><td> 66.5 </td><td> 69.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Peugeot</td><td>208</td><td>1.2</td><td>2017</td><td> 44.9 </td><td> 61.8 </td><td> 65.0 </td><td> 68.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Peugeot</td><td>208</td><td>1.6d</td><td>2017</td><td> 47.9 </td><td> 64.7 </td><td> 65.5 </td><td> 66.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Peugeot</td><td>208</td><td>GTI</td><td>2017</td><td> 46.9 </td><td> 63.7 </td><td> 67.0 </td><td> 70.3 </td><td> 73.0 </td><td> 76.8 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6</td><td>2008</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 67.1 </td><td> 69.0 </td><td> 71.3 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6 Stationcar</td><td>2008</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 65.0 </td><td> 67.2 </td><td> 69.6 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>2.0 HDiF</td><td>2008</td><td> 41.3 </td><td> 50.9 </td><td> 58.5 </td><td> 61.3 </td><td> 63.7 </td><td> 66.3 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>XT2.0 16V HDI</td><td>2008</td><td> 44.9 </td><td> 60.0 </td><td> 65.0 </td><td> 67.0 </td><td> 69.0 </td><td> 71.0 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6 VTi CC</td><td>2009</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 66.8 </td><td> 68.7 </td><td> 71.0 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6 VTI Stationcar</td><td>2009</td><td> 39.2 </td><td> 59.6 </td><td> 62.3 </td><td> 65.2 </td><td> 68.4 </td><td> 71.2 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6 CC </td><td>2010</td><td> 35.6 </td><td> 61.3 </td><td> 63.1 </td><td> 66.7 </td><td> 67.4 </td><td> 69.2 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6 THP GTI</td><td>2010</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 65.7 </td><td> 67.1 </td><td> 68.9 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6 VTi</td><td>2010</td><td> 43.8 </td><td> 53.9 </td><td> 62.0 </td><td> 66.8 </td><td> 67.4 </td><td> 68.3 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6 HDI</td><td>2011</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 67.1 </td><td> 68.7 </td><td> 70.7 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6 HDI</td><td>2011</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 67.1 </td><td> 68.7 </td><td> 70.7 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6 THP Stationcar</td><td>2011</td><td> 37.0 </td><td> 61.3 </td><td> 62.5 </td><td> 63.0 </td><td> 67.4 </td><td> 69.3 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>CC 1.6</td><td>2012</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 68.0 </td><td> 69.2 </td><td> 70.8 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6</td><td>2013</td><td> 37.6 </td><td> 56.6 </td><td> 59.3 </td><td> 61.8 </td><td> 65.7 </td><td> 68.5 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.2</td><td>2014</td><td> 43.5 </td><td> 58.1 </td><td> 61.6 </td><td> 64.3 </td><td> 66.9 </td><td> 69.4 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6D</td><td>2014</td><td> 44.0 </td><td> 58.7 </td><td> 62.5 </td><td> 64.8 </td><td> 67.7 </td><td> 69.4 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>SW 1.6</td><td>2014</td><td> 43.7 </td><td> 59.1 </td><td> 60.8 </td><td> 64.8 </td><td> 67.3 </td><td> 69.4 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.2</td><td>2015</td><td> 38.2 </td><td> 56.1 </td><td> 61.1 </td><td> 65.1 </td><td> 68.6 </td><td> 70.1 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.2 Stationcar</td><td>2016</td><td> 38.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.6D</td><td>2016</td><td> 46.9 </td><td> 61.8 </td><td> 64.0 </td><td> 66.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>GTI</td><td>2016</td><td> 40.9 </td><td> 61.8 </td><td> 65.0 </td><td> 67.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Peugeot</td><td>308</td><td>1.2 stationcar</td><td>2017</td><td> 38.5 </td><td> 54.1 </td><td> 58.8 </td><td> 62.8 </td><td> 68.8 </td><td> 68.9 </td></tr>
<tr><td>Peugeot</td><td>407</td><td>2.0 Stationcar</td><td>2009</td><td> 43.1 </td><td> 53.0 </td><td> 61.0 </td><td> 64.7 </td><td> 66.3 </td><td> 68.3 </td></tr>
<tr><td>Peugeot</td><td>508</td><td>1.6 E-HDI</td><td>2011</td><td> 44.2 </td><td> 59.0 </td><td> 62.0 </td><td> 64.5 </td><td> 68.0 </td><td> 70.0 </td></tr>
<tr><td>Peugeot</td><td>508</td><td>1.6 e-HDI</td><td>2011</td><td> 43.2 </td><td> 53.2 </td><td> 61.2 </td><td> 65.1 </td><td> 66.5 </td><td> 68.3 </td></tr>
<tr><td>Peugeot</td><td>508</td><td>1.6 E-HDI Stationcar</td><td>2011</td><td> 50.8 </td><td> 58.6 </td><td> 61.5 </td><td> 64.4 </td><td> 70.0 </td><td> 71.5 </td></tr>
<tr><td>Peugeot</td><td>508</td><td>1.6 E-HDI</td><td>2012</td><td> 43.0 </td><td> 55.6 </td><td> 58.6 </td><td> 62.2 </td><td> 66.3 </td><td> 69.9 </td></tr>
<tr><td>Peugeot</td><td>508</td><td>2.0 HDI Stationcar</td><td>2012</td><td> 43.4 </td><td> 53.4 </td><td> 61.4 </td><td> 65.8 </td><td> 66.7 </td><td> 68.0 </td></tr>
<tr><td>Peugeot</td><td>508</td><td>2.0 Hybrid Stationcar</td><td>2012</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 66.0 </td><td> 68.1 </td><td> 70.4 </td></tr>
<tr><td>Peugeot</td><td>508</td><td>1.6D Stationcar</td><td>2015</td><td> 48.3 </td><td> 58.4 </td><td> 62.4 </td><td> 65.1 </td><td> 68.5 </td><td> 71.5 </td></tr>
<tr><td>Peugeot</td><td>2008</td><td>1.6 THP</td><td>2010</td><td> 44.3 </td><td> 54.5 </td><td> 62.7 </td><td> 65.4 </td><td> 68.2 </td><td> 71.4 </td></tr>
<tr><td>Peugeot</td><td>2008</td><td>1.2</td><td>2013</td><td> 45.7 </td><td> 62.8 </td><td> 65.4 </td><td> 67.1 </td><td> 70.3 </td><td> 73.0 </td></tr>
<tr><td>Peugeot</td><td>2008</td><td>1.2</td><td>2014</td><td> 40.4 </td><td> 57.5 </td><td> 62.6 </td><td> 65.2 </td><td> 68.9 </td><td> 72.3 </td></tr>
<tr><td>Peugeot</td><td>2008</td><td>1.2</td><td>2015</td><td> 39.1 </td><td> 59.3 </td><td> 63.7 </td><td> 67.2 </td><td> 71.4 </td><td> 74.0 </td></tr>
<tr><td>Peugeot</td><td>2008</td><td>1.2</td><td>2017</td><td> 39.3 </td><td> 56.7 </td><td> 61.1 </td><td> 64.1 </td><td> 70.2 </td><td> 70.3 </td></tr>
<tr><td>Peugeot</td><td>3008</td><td>1.6 THP</td><td>2009</td><td> 37.0 </td><td> 57.2 </td><td> 61.9 </td><td> 63.5 </td><td> 67.1 </td><td> 68.2 </td></tr>
<tr><td>Peugeot</td><td>3008</td><td>1.6 THP</td><td>2009</td><td> 44.7 </td><td> 55.0 </td><td> 63.3 </td><td> 66.8 </td><td> 68.9 </td><td> 71.2 </td></tr>
<tr><td>Peugeot</td><td>3008</td><td>2.0 HDiF</td><td>2010</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 65.4 </td><td> 68.1 </td><td> 71.2 </td></tr>
<tr><td>Peugeot</td><td>3008</td><td>1.6 VTI</td><td>2012</td><td> 37.5 </td><td> 58.7 </td><td> 62.6 </td><td> 66.0 </td><td> 69.6 </td><td> 72.4 </td></tr>
<tr><td>Peugeot</td><td>3008</td><td>1.2</td><td>2017</td><td> 36.3 </td><td> 56.3 </td><td> 60.3 </td><td> 63.6 </td><td> 69.0 </td><td> 69.1 </td></tr>
<tr><td>Peugeot</td><td>3008</td><td>2.0d</td><td>2017</td><td> 47.9 </td><td> 57.8 </td><td> 60.5 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Peugeot</td><td>5008</td><td>1.8 THP</td><td>2010</td><td> 43.3 </td><td> 57.8 </td><td> 63.3 </td><td> 66.0 </td><td> 68.3 </td><td> 70.8 </td></tr>
<tr><td>Peugeot</td><td>5008</td><td>1.6</td><td>2017</td><td> 38.9 </td><td> 58.8 </td><td> 62.0 </td><td> 65.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Peugeot</td><td>RCZ</td><td>1.6 THP</td><td>2010</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 66.1 </td><td> 68.3 </td><td> 70.7 </td></tr>
<tr><td>Peugeot</td><td>RCZ</td><td>1.6 THP 200</td><td>2011</td><td> 43.8 </td><td> 53.9 </td><td> 62.0 </td><td> 66.4 </td><td> 67.4 </td><td> 68.8 </td></tr>
<tr><td>Pontiac</td><td>G8</td><td>3.6 V6</td><td>2008</td><td> 43.8 </td><td> 55.6 </td><td> 63.0 </td><td> 66.8 </td><td> 70.4 </td><td> 74.1 </td></tr>
<tr><td>Pontiac</td><td>G8</td><td>GT</td><td>2008</td><td> 48.5 </td><td> 58.1 </td><td> 64.1 </td><td> 67.2 </td><td> 69.9 </td><td> 72.5 </td></tr>
<tr><td>Porsche</td><td>718</td><td>Boxter S</td><td>2016</td><td> 53.8 </td><td> 62.7 </td><td> 67.0 </td><td> 70.3 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>Porsche</td><td>718</td><td>Cayman</td><td>2016</td><td> 52.8 </td><td> 66.7 </td><td> 69.0 </td><td> 71.3 </td><td> 72.1 </td><td> 75.8 </td></tr>
<tr><td>Porsche</td><td>718</td><td>Boxter S</td><td>2017</td><td> 52.8 </td><td> 63.7 </td><td> 67.0 </td><td> 70.3 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>Porsche</td><td>911</td><td>GT2</td><td>2008</td><td> 63.7 </td><td> 68.2 </td><td> 71.4 </td><td> 71.8 </td><td> 76.9 </td><td> 82.1 </td></tr>
<tr><td>Porsche</td><td>911</td><td>GT3</td><td>2010</td><td> 57.4 </td><td> 66.3 </td><td> 72.1 </td><td> 74.4 </td><td> 79.3 </td><td> 84.2 </td></tr>
<tr><td>Porsche</td><td>911</td><td>GT2 RS</td><td>2011</td><td> 61.7 </td><td> 67.1 </td><td> 70.6 </td><td> 71.8 </td><td> 75.4 </td><td> 79.1 </td></tr>
<tr><td>Porsche</td><td>911</td><td>GTS</td><td>2011</td><td> 49.7 </td><td> 58.9 </td><td> 65.1 </td><td> 67.0 </td><td> 73.9 </td><td> 80.9 </td></tr>
<tr><td>Porsche</td><td>911</td><td>Carrera S Cabrio</td><td>2012</td><td> 48.6 </td><td> 59.8 </td><td> 68.8 </td><td> 73.7 </td><td> 74.8 </td><td> 76.3 </td></tr>
<tr><td>Porsche</td><td>911</td><td>S</td><td>2012</td><td> 48.8 </td><td> 58.0 </td><td> 64.2 </td><td> 66.0 </td><td> 73.3 </td><td> 80.6 </td></tr>
<tr><td>Porsche</td><td>911</td><td>Carrera S</td><td>2013</td><td> 52.5 </td><td> 59.6 </td><td> 64.7 </td><td> 65.2 </td><td> 73.9 </td><td> 82.6 </td></tr>
<tr><td>Porsche</td><td>911</td><td>Targa</td><td>2014</td><td> 44.9 </td><td> 63.2 </td><td> 66.1 </td><td> 68.9 </td><td> 73.5 </td><td> 75.3 </td></tr>
<tr><td>Porsche</td><td>911</td><td>Cabrio</td><td>2016</td><td> 53.8 </td><td> 63.7 </td><td> 67.0 </td><td> 70.3 </td><td> 73.0 </td><td> 76.8 </td></tr>
<tr><td>Porsche</td><td>911</td><td>Carrera S</td><td>2016</td><td> 54.2 </td><td> 65.3 </td><td> 67.8 </td><td> 70.3 </td><td> 74.1 </td><td> 77.9 </td></tr>
<tr><td>Porsche</td><td>911</td><td>Carrera S Cabrio</td><td>2016</td><td> 54.2 </td><td> 64.3 </td><td> 67.3 </td><td> 70.3 </td><td> 73.1 </td><td> 76.9 </td></tr>
<tr><td>Porsche</td><td>911</td><td>Turbo</td><td>2016</td><td> 56.8 </td><td> 65.7 </td><td> 69.5 </td><td> 71.9 </td><td> 73.0 </td><td> 76.8 </td></tr>
<tr><td>Porsche</td><td>911</td><td>Turbo</td><td>2017</td><td> 55.8 </td><td> 62.7 </td><td> 67.5 </td><td> 69.9 </td><td> 72.1 </td><td> 75.8 </td></tr>
<tr><td>Porsche</td><td>Boxter</td><td>Spyder</td><td>2011</td><td> 51.0 </td><td> 58.5 </td><td> 63.4 </td><td> 65.1 </td><td> 69.9 </td><td> 74.8 </td></tr>
<tr><td>Porsche</td><td>Boxter</td><td>S</td><td>2012</td><td> 49.2 </td><td> 57.8 </td><td> 63.5 </td><td> 65.3 </td><td> 71.3 </td><td> 77.3 </td></tr>
<tr><td>Porsche</td><td>Boxter</td><td>S</td><td>2012</td><td> 43.4 </td><td> 53.4 </td><td> 61.4 </td><td> 65.6 </td><td> 66.7 </td><td> 68.2 </td></tr>
<tr><td>Porsche</td><td>Cayenne</td><td>GTS</td><td>2008</td><td> 44.1 </td><td> 54.3 </td><td> 62.5 </td><td> 65.8 </td><td> 68.0 </td><td> 70.4 </td></tr>
<tr><td>Porsche</td><td>Cayenne</td><td>Diesel</td><td>2009</td><td> 45.5 </td><td> 56.0 </td><td> 64.4 </td><td> 68.1 </td><td> 70.0 </td><td> 72.3 </td></tr>
<tr><td>Porsche</td><td>Cayenne</td><td>Turbo</td><td>2010</td><td> 44.1 </td><td> 54.3 </td><td> 62.5 </td><td> 65.5 </td><td> 68.0 </td><td> 70.8 </td></tr>
<tr><td>Porsche</td><td>Cayenne</td><td>S Hybrid</td><td>2011</td><td> 44.5 </td><td> 53.5 </td><td> 59.3 </td><td> 61.9 </td><td> 65.5 </td><td> 69.1 </td></tr>
<tr><td>Porsche</td><td>Cayenne</td><td>Diesel</td><td>2012</td><td> 42.3 </td><td> 52.1 </td><td> 59.9 </td><td> 63.1 </td><td> 65.2 </td><td> 67.5 </td></tr>
<tr><td>Porsche</td><td>Cayenne</td><td>Turbo</td><td>2014</td><td> 48.9 </td><td> 57.8 </td><td> 60.5 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Porsche</td><td>Cayenne</td><td>Turbo S</td><td>2016</td><td> 47.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Porsche</td><td>Cayman</td><td>&nbsp;</td><td>2008</td><td> 46.3 </td><td> 57.0 </td><td> 65.6 </td><td> 68.5 </td><td> 71.4 </td><td> 74.7 </td></tr>
<tr><td>Porsche</td><td>Cayman</td><td>R</td><td>2012</td><td> 54.4 </td><td> 61.3 </td><td> 65.9 </td><td> 67.2 </td><td> 72.7 </td><td> 78.2 </td></tr>
<tr><td>Porsche</td><td>Cayman</td><td>2.7</td><td>2013</td><td> 45.8 </td><td> 55.7 </td><td> 62.5 </td><td> 64.3 </td><td> 72.4 </td><td> 80.5 </td></tr>
<tr><td>Porsche</td><td>Cayman</td><td>S</td><td>2014</td><td> 55.4 </td><td> 61.6 </td><td> 65.8 </td><td> 66.8 </td><td> 72.2 </td><td> 77.7 </td></tr>
<tr><td>Porsche</td><td>Cayman</td><td>S</td><td>2017</td><td> 49.9 </td><td> 63.7 </td><td> 67.5 </td><td> 71.3 </td><td> 72.1 </td><td> 75.8 </td></tr>
<tr><td>Porsche</td><td>Macan</td><td>S Diesel</td><td>2014</td><td> 41.2 </td><td> 53.5 </td><td> 57.9 </td><td> 60.5 </td><td> 64.4 </td><td> 66.5 </td></tr>
<tr><td>Porsche</td><td>Macan</td><td>S</td><td>2015</td><td> 45.4 </td><td> 55.2 </td><td> 60.2 </td><td> 63.1 </td><td> 66.3 </td><td> 69.6 </td></tr>
<tr><td>Porsche</td><td>Macan</td><td>Diesel</td><td>2016</td><td> 45.1 </td><td> 60.2 </td><td> 61.7 </td><td> 63.3 </td><td> 65.3 </td><td> 68.7 </td></tr>
<tr><td>Porsche</td><td>Macan</td><td>GTS</td><td>2016</td><td> 44.9 </td><td> 58.8 </td><td> 61.0 </td><td> 63.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Porsche</td><td>Macan</td><td>2.0</td><td>2017</td><td> 38.9 </td><td> 55.8 </td><td> 60.5 </td><td> 63.5 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Porsche</td><td>Macan</td><td>3.0d</td><td>2017</td><td> 41.6 </td><td> 55.6 </td><td> 59.6 </td><td> 60.9 </td><td> 66.1 </td><td> 66.1 </td></tr>
<tr><td>Porsche</td><td>Panamera</td><td>Turbo</td><td>2009</td><td> 47.7 </td><td> 58.1 </td><td> 62.6 </td><td> 64.6 </td><td> 68.6 </td><td> 70.1 </td></tr>
<tr><td>Porsche</td><td>Panamera</td><td>4S</td><td>2010</td><td> 43.2 </td><td> 57.6 </td><td> 62.5 </td><td> 65.4 </td><td> 69.2 </td><td> 70.1 </td></tr>
<tr><td>Porsche</td><td>Panamera</td><td>3.6 V6</td><td>2011</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 64.8 </td><td> 67.6 </td><td> 70.8 </td></tr>
<tr><td>Porsche</td><td>Panamera</td><td>Turbo 4.8 V8</td><td>2011</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 65.7 </td><td> 67.5 </td><td> 69.7 </td></tr>
<tr><td>Porsche</td><td>Panamera</td><td>S Hybrid 3.0 V6</td><td>2012</td><td> 43.5 </td><td> 53.5 </td><td> 61.5 </td><td> 64.8 </td><td> 67.0 </td><td> 69.4 </td></tr>
<tr><td>Porsche</td><td>Panamera</td><td>S E-Hybrid</td><td>2013</td><td> 39.1 </td><td> 52.9 </td><td> 58.6 </td><td> 60.6 </td><td> 64.9 </td><td> 69.6 </td></tr>
<tr><td>Porsche</td><td>Panamera</td><td>S E-hybrid</td><td>2016</td><td> 41.9 </td><td> 58.8 </td><td> 61.0 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Porsche</td><td>Panamera</td><td>Turbo</td><td>2017</td><td> 46.9 </td><td> 56.8 </td><td> 61.0 </td><td> 63.7 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Range Rover</td><td>0</td><td>5.0 V8</td><td>2013</td><td> 42.8 </td><td> 52.3 </td><td> 58.2 </td><td> 61.2 </td><td> 63.9 </td><td> 66.6 </td></tr>
<tr><td>Range Rover</td><td>Evoque</td><td>TDV8</td><td>2008</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 66.0 </td><td> 68.1 </td><td> 70.4 </td></tr>
<tr><td>Range Rover</td><td>Evoque</td><td>2.2</td><td>2011</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 65.2 </td><td> 67.1 </td><td> 69.4 </td></tr>
<tr><td>Range Rover</td><td>Evoque</td><td>2.2</td><td>2014</td><td> 44.9 </td><td> 60.1 </td><td> 64.5 </td><td> 67.2 </td><td> 68.1 </td><td> 70.3 </td></tr>
<tr><td>Range Rover</td><td>Evoque</td><td>2.0D</td><td>2016</td><td> 46.8 </td><td> 53.7 </td><td> 59.4 </td><td> 62.8 </td><td> 66.8 </td><td> 68.9 </td></tr>
<tr><td>Range Rover</td><td>Sport</td><td>TDV6</td><td>2013</td><td> 43.2 </td><td> 55.1 </td><td> 59.4 </td><td> 61.2 </td><td> 65.3 </td><td> 68.2 </td></tr>
<tr><td>Range Rover</td><td>Sport</td><td>5.0 V8</td><td>2014</td><td> 47.3 </td><td> 54.6 </td><td> 59.4 </td><td> 61.3 </td><td> 65.2 </td><td> 69.1 </td></tr>
<tr><td>Range Rover</td><td>Sport</td><td>5.0 V8</td><td>2014</td><td> 48.1 </td><td> 58.2 </td><td> 59.7 </td><td> 61.2 </td><td> 65.3 </td><td> 68.7 </td></tr>
<tr><td>Range Rover</td><td>Velar</td><td>2.0d</td><td>2017</td><td> 44.2 </td><td> 53.6 </td><td> 58.1 </td><td> 60.6 </td><td> 65.6 </td><td> 65.7 </td></tr>
<tr><td>Renault</td><td>Captur</td><td>1.2</td><td>2013</td><td> 44.3 </td><td> 59.7 </td><td> 64.4 </td><td> 65.3 </td><td> 68.2 </td><td> 69.4 </td></tr>
<tr><td>Renault</td><td>Captur</td><td>0.9</td><td>2014</td><td> 40.6 </td><td> 57.4 </td><td> 62.2 </td><td> 66.1 </td><td> 68.4 </td><td> 72.0 </td></tr>
<tr><td>Renault</td><td>Captur</td><td>1.2</td><td>2015</td><td> 36.3 </td><td> 58.6 </td><td> 63.8 </td><td> 66.3 </td><td> 69.4 </td><td> 73.2 </td></tr>
<tr><td>Renault</td><td>Captur</td><td>1.2</td><td>2017</td><td> 48.9 </td><td> 58.4 </td><td> 61.2 </td><td> 65.0 </td><td> 71.3 </td><td> 71.3 </td></tr>
<tr><td>Renault</td><td>Clio</td><td>1.2</td><td>2008</td><td> 38.8 </td><td> 59.0 </td><td> 62.8 </td><td> 65.3 </td><td> 68.5 </td><td> 71.8 </td></tr>
<tr><td>Renault</td><td>Clio</td><td>1.2 Stationcar</td><td>2008</td><td> 46.4 </td><td> 57.1 </td><td> 65.7 </td><td> 66.2 </td><td> 71.5 </td><td> 77.5 </td></tr>
<tr><td>Renault</td><td>Clio</td><td>1.2</td><td>2009</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 66.4 </td><td> 68.3 </td><td> 70.6 </td></tr>
<tr><td>Renault</td><td>Clio</td><td>1.2</td><td>2010</td><td> 45.4 </td><td> 55.8 </td><td> 64.2 </td><td> 67.5 </td><td> 69.9 </td><td> 72.5 </td></tr>
<tr><td>Renault</td><td>Clio</td><td>TCE 100</td><td>2010</td><td> 39.0 </td><td> 59.3 </td><td> 62.6 </td><td> 66.4 </td><td> 68.5 </td><td> 70.5 </td></tr>
<tr><td>Renault</td><td>Clio</td><td>0.9</td><td>2012</td><td> 45.5 </td><td> 58.3 </td><td> 63.4 </td><td> 68.0 </td><td> 71.3 </td><td> 74.8 </td></tr>
<tr><td>Renault</td><td>Clio</td><td>0.9</td><td>2014</td><td> 41.4 </td><td> 59.6 </td><td> 64.3 </td><td> 68.5 </td><td> 71.2 </td><td> 73.5 </td></tr>
<tr><td>Renault</td><td>Clio</td><td>0.9</td><td>2017</td><td> 41.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Renault</td><td>Clio</td><td>1.5d</td><td>2017</td><td> 46.9 </td><td> 60.8 </td><td> 64.0 </td><td> 65.6 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Renault</td><td>Clio</td><td>RS Trophy</td><td>2017</td><td> 44.9 </td><td> 63.7 </td><td> 67.0 </td><td> 70.3 </td><td> 71.1 </td><td> 74.7 </td></tr>
<tr><td>Renault</td><td>Espace</td><td>2.0 DCI 16V </td><td>2008</td><td> 49.9 </td><td> 60.0 </td><td> 61.2 </td><td> 63.9 </td><td> 68.2 </td><td> 70.3 </td></tr>
<tr><td>Renault</td><td>Espace</td><td>1.6</td><td>2015</td><td> 42.3 </td><td> 55.2 </td><td> 59.2 </td><td> 62.6 </td><td> 66.0 </td><td> 69.7 </td></tr>
<tr><td>Renault</td><td>Espace</td><td>1.6D</td><td>2016</td><td> 44.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Renault</td><td>Fluence</td><td>&nbsp;</td><td>2012</td><td> 46.2 </td><td> 58.4 </td><td> 64.2 </td><td> 66.6 </td><td> 71.1 </td><td> 76.2 </td></tr>
<tr><td>Renault</td><td>Grand Espace</td><td>3.5 V6</td><td>2008</td><td> 43.2 </td><td> 53.1 </td><td> 61.1 </td><td> 64.1 </td><td> 66.5 </td><td> 69.1 </td></tr>
<tr><td>Renault</td><td>Grand Modus</td><td>1.2</td><td>2009</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 64.5 </td><td> 67.6 </td><td> 71.1 </td></tr>
<tr><td>Renault</td><td>Grand Scenic</td><td>1.4</td><td>2009</td><td> 44.1 </td><td> 54.2 </td><td> 62.4 </td><td> 64.7 </td><td> 67.9 </td><td> 71.5 </td></tr>
<tr><td>Renault</td><td>Grand Scenic</td><td>1.5</td><td>2012</td><td> 43.5 </td><td> 53.5 </td><td> 61.5 </td><td> 65.3 </td><td> 66.9 </td><td> 68.9 </td></tr>
<tr><td>Renault</td><td>Kadjar</td><td>1.2</td><td>2015</td><td> 44.0 </td><td> 56.4 </td><td> 61.7 </td><td> 64.6 </td><td> 67.8 </td><td> 70.6 </td></tr>
<tr><td>Renault</td><td>Kadjar</td><td>1.6D</td><td>2015</td><td> 43.6 </td><td> 60.2 </td><td> 63.6 </td><td> 66.9 </td><td> 69.6 </td><td> 71.3 </td></tr>
<tr><td>Renault</td><td>Kadjar</td><td>1.2</td><td>2017</td><td> 38.2 </td><td> 55.8 </td><td> 60.9 </td><td> 63.9 </td><td> 71.0 </td><td> 71.1 </td></tr>
<tr><td>Renault</td><td>Kangoo</td><td>1.6</td><td>2008</td><td> 45.6 </td><td> 56.2 </td><td> 64.6 </td><td> 68.3 </td><td> 70.2 </td><td> 72.5 </td></tr>
<tr><td>Renault</td><td>Kangoo</td><td>1.6 16V 110</td><td>2008</td><td> 42.3 </td><td> 63.3 </td><td> 68.4 </td><td> 72.6 </td><td> 74.8 </td><td> 76.4 </td></tr>
<tr><td>Renault</td><td>Koleos</td><td>2.0 dCI</td><td>2008</td><td> 43.5 </td><td> 53.5 </td><td> 61.5 </td><td> 63.8 </td><td> 67.0 </td><td> 70.6 </td></tr>
<tr><td>Renault</td><td>Koleos</td><td>2.0 DCI 175</td><td>2008</td><td> 42.2 </td><td> 61.5 </td><td> 64.3 </td><td> 66.9 </td><td> 70.2 </td><td> 72.1 </td></tr>
<tr><td>Renault</td><td>Koleos</td><td>1.6</td><td>2017</td><td> 46.2 </td><td> 54.5 </td><td> 62.3 </td><td> 65.4 </td><td> 71.1 </td><td> 71.2 </td></tr>
<tr><td>Renault</td><td>Laguna</td><td>2.0</td><td>2008</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 66.2 </td><td> 68.0 </td><td> 70.2 </td></tr>
<tr><td>Renault</td><td>Laguna</td><td>2.0 dCI</td><td>2008</td><td> 41.2 </td><td> 50.7 </td><td> 58.3 </td><td> 61.2 </td><td> 63.5 </td><td> 66.0 </td></tr>
<tr><td>Renault</td><td>Laguna</td><td>2.0 Stationcar</td><td>2008</td><td> 43.7 </td><td> 53.8 </td><td> 61.9 </td><td> 66.5 </td><td> 67.3 </td><td> 68.5 </td></tr>
<tr><td>Renault</td><td>Laguna</td><td>3.5 V6 Coupe</td><td>2009</td><td> 41.3 </td><td> 58.0 </td><td> 62.0 </td><td> 64.0 </td><td> 66.0 </td><td> 67.0 </td></tr>
<tr><td>Renault</td><td>Laguna</td><td>1.5 D Stationcar</td><td>2011</td><td> 43.4 </td><td> 53.4 </td><td> 61.5 </td><td> 65.1 </td><td> 66.8 </td><td> 68.9 </td></tr>
<tr><td>Renault</td><td>Laguna</td><td>1.5 DCI</td><td>2011</td><td> 44.9 </td><td> 62.0 </td><td> 65.0 </td><td> 66.5 </td><td> 69.0 </td><td> 72.0 </td></tr>
<tr><td>Renault</td><td>Laguna</td><td>1.5 DCI Stationcar</td><td>2011</td><td> 51.9 </td><td> 58.6 </td><td> 63.7 </td><td> 66.6 </td><td> 68.6 </td><td> 72.0 </td></tr>
<tr><td>Renault</td><td>Laguna</td><td>1.5 DCI Stationcar</td><td>2015</td><td> 45.6 </td><td> 57.1 </td><td> 62.8 </td><td> 66.8 </td><td> 69.4 </td><td> 71.6 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>1.4 Stationcar</td><td>2009</td><td> 45.8 </td><td> 56.3 </td><td> 64.8 </td><td> 67.9 </td><td> 70.5 </td><td> 73.5 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>1.6</td><td>2009</td><td> 46.7 </td><td> 57.5 </td><td> 66.1 </td><td> 68.1 </td><td> 72.0 </td><td> 76.4 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>1.6 16V</td><td>2009</td><td> 42.2 </td><td> 63.6 </td><td> 66.2 </td><td> 67.5 </td><td> 69.5 </td><td> 72.0 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>1.9 dCI</td><td>2009</td><td> 44.8 </td><td> 55.1 </td><td> 63.4 </td><td> 67.1 </td><td> 68.9 </td><td> 71.1 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>TCE 130 Stationcar</td><td>2009</td><td> 39.9 </td><td> 58.7 </td><td> 62.8 </td><td> 65.3 </td><td> 67.7 </td><td> 72.2 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>1.6 CC </td><td>2010</td><td> 37.1 </td><td> 59.4 </td><td> 62.5 </td><td> 64.8 </td><td> 67.7 </td><td> 69.6 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>GT 2.0 Coupe</td><td>2011</td><td> 44.5 </td><td> 63.1 </td><td> 64.9 </td><td> 66.5 </td><td> 68.4 </td><td> 71.0 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>1.2 Coupe</td><td>2012</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 65.2 </td><td> 67.6 </td><td> 70.2 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>1.5 D Stationcar</td><td>2012</td><td> 43.4 </td><td> 53.4 </td><td> 61.4 </td><td> 65.9 </td><td> 66.7 </td><td> 67.8 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>110 DCI Stationcar</td><td>2012</td><td> 44.0 </td><td> 57.6 </td><td> 61.5 </td><td> 64.9 </td><td> 67.8 </td><td> 74.6 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>1.2</td><td>2016</td><td> 45.4 </td><td> 59.6 </td><td> 63.4 </td><td> 65.6 </td><td> 68.2 </td><td> 69.8 </td></tr>
<tr><td>Renault</td><td>Megane</td><td>1.6D</td><td>2016</td><td> 43.9 </td><td> 61.8 </td><td> 64.0 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Renault</td><td>Scenic</td><td>2.0</td><td>2008</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 66.0 </td><td> 68.1 </td><td> 70.4 </td></tr>
<tr><td>Renault</td><td>Scenic</td><td>TCE 130</td><td>2009</td><td> 38.4 </td><td> 61.5 </td><td> 63.8 </td><td> 66.7 </td><td> 69.3 </td><td> 72.8 </td></tr>
<tr><td>Renault</td><td>Scenic</td><td>2.0 dCI</td><td>2010</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 65.6 </td><td> 68.4 </td><td> 71.6 </td></tr>
<tr><td>Renault</td><td>Scenic</td><td>TCE 130</td><td>2010</td><td> 36.4 </td><td> 59.5 </td><td> 63.3 </td><td> 65.1 </td><td> 67.2 </td><td> 70.5 </td></tr>
<tr><td>Renault</td><td>Scenic</td><td>1.2</td><td>2017</td><td> 36.6 </td><td> 52.6 </td><td> 59.7 </td><td> 62.3 </td><td> 69.8 </td><td> 69.9 </td></tr>
<tr><td>Renault</td><td>Scenic</td><td>1.6d</td><td>2017</td><td> 45.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Renault</td><td>Talisman</td><td>1.5D</td><td>2016</td><td> 45.7 </td><td> 55.3 </td><td> 61.3 </td><td> 63.3 </td><td> 66.6 </td><td> 70.4 </td></tr>
<tr><td>Renault</td><td>Talisman</td><td>1.6D</td><td>2016</td><td> 42.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Renault</td><td>Talisman</td><td>1.6d</td><td>2017</td><td> 47.9 </td><td> 58.8 </td><td> 60.5 </td><td> 62.2 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Renault</td><td>Twingo</td><td>1.2</td><td>2008</td><td> 46.7 </td><td> 64.4 </td><td> 69.4 </td><td> 73.6 </td><td> 77.3 </td><td> 81.5 </td></tr>
<tr><td>Renault</td><td>Twingo</td><td>RS</td><td>2008</td><td> 47.1 </td><td> 58.0 </td><td> 66.7 </td><td> 70.5 </td><td> 72.6 </td><td> 74.9 </td></tr>
<tr><td>Renault</td><td>Twingo</td><td>1.2</td><td>2009</td><td> 46.2 </td><td> 56.8 </td><td> 65.3 </td><td> 69.2 </td><td> 71.0 </td><td> 73.2 </td></tr>
<tr><td>Renault</td><td>Twingo</td><td>1.2 60</td><td>2009</td><td> 49.5 </td><td> 65.2 </td><td> 70.5 </td><td> 72.5 </td><td> 73.5 </td><td> 77.5 </td></tr>
<tr><td>Renault</td><td>Twingo</td><td>1.2</td><td>2012</td><td> 46.3 </td><td> 59.9 </td><td> 64.7 </td><td> 68.4 </td><td> 71.3 </td><td> 75.3 </td></tr>
<tr><td>Renault</td><td>Twingo</td><td>1.2</td><td>2013</td><td> 43.2 </td><td> 61.6 </td><td> 66.6 </td><td> 70.4 </td><td> 73.1 </td><td> 75.8 </td></tr>
<tr><td>Renault</td><td>Twingo</td><td>1.0</td><td>2014</td><td> 41.6 </td><td> 62.2 </td><td> 63.8 </td><td> 67.6 </td><td> 71.4 </td><td> 73.5 </td></tr>
<tr><td>Renault</td><td>Twingo</td><td>0.9</td><td>2016</td><td> 47.9 </td><td> 60.8 </td><td> 64.0 </td><td> 67.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Renault</td><td>Wind</td><td>1.2</td><td>2010</td><td> 46.3 </td><td> 57.0 </td><td> 65.5 </td><td> 69.2 </td><td> 71.3 </td><td> 73.6 </td></tr>
<tr><td>Renault</td><td>Zoe</td><td>&nbsp;</td><td>2013</td><td> 45.2 </td><td> 59.8 </td><td> 63.0 </td><td> 66.8 </td><td> 69.6 </td><td> 72.9 </td></tr>
<tr><td>Renault</td><td>Zoe</td><td>EV</td><td>2017</td><td> 46.1 </td><td> 55.4 </td><td> 61.6 </td><td> 65.5 </td><td> 71.0 </td><td> 71.1 </td></tr>
<tr><td>Rolls Royce</td><td>Wraith</td><td>6.6 V12</td><td>2014</td><td> 42.0 </td><td> 50.6 </td><td> 56.2 </td><td> 58.2 </td><td> 63.5 </td><td> 68.8 </td></tr>
<tr><td>Saab</td><td>9-3</td><td>1.8t</td><td>2008</td><td> 44.1 </td><td> 54.3 </td><td> 62.5 </td><td> 67.6 </td><td> 67.9 </td><td> 68.5 </td></tr>
<tr><td>Saab</td><td>9-3</td><td>1.9 TTiD Stationcar</td><td>2008</td><td> 44.7 </td><td> 55.0 </td><td> 63.3 </td><td> 66.1 </td><td> 68.9 </td><td> 72.1 </td></tr>
<tr><td>Saab</td><td>9-3</td><td>X 2.0</td><td>2009</td><td> 44.5 </td><td> 54.7 </td><td> 62.9 </td><td> 66.5 </td><td> 68.4 </td><td> 70.7 </td></tr>
<tr><td>Saab</td><td>9-5</td><td>2.0T</td><td>2010</td><td> 42.4 </td><td> 60.9 </td><td> 62.2 </td><td> 65.3 </td><td> 66.7 </td><td> 68.0 </td></tr>
<tr><td>Saab</td><td>9-5</td><td>Aero</td><td>2010</td><td> 46.4 </td><td> 56.2 </td><td> 62.3 </td><td> 65.6 </td><td> 68.1 </td><td> 70.6 </td></tr>
<tr><td>Saturn</td><td>Astra</td><td>1.8</td><td>2008</td><td> 45.3 </td><td> 58.9 </td><td> 67.2 </td><td> 72.2 </td><td> 74.1 </td><td> 76.1 </td></tr>
<tr><td>Saturn</td><td>Vue</td><td>3.6 V6</td><td>2008</td><td> 53.7 </td><td> 61.2 </td><td> 66.1 </td><td> 68.0 </td><td> 71.9 </td><td> 75.7 </td></tr>
<tr><td>Scion</td><td>FR-S</td><td>2.0</td><td>2012</td><td> 44.1 </td><td> 56.7 </td><td> 64.7 </td><td> 68.6 </td><td> 73.1 </td><td> 77.6 </td></tr>
<tr><td>Scion</td><td>iQ</td><td>1.3</td><td>2012</td><td> 42.7 </td><td> 55.6 </td><td> 63.6 </td><td> 68.2 </td><td> 70.3 </td><td> 72.4 </td></tr>
<tr><td>Scion</td><td>tC</td><td>2.5</td><td>2011</td><td> 43.5 </td><td> 56.0 </td><td> 63.7 </td><td> 68.2 </td><td> 70.0 </td><td> 71.8 </td></tr>
<tr><td>Scion</td><td>xB</td><td>2.4</td><td>2008</td><td> 42.7 </td><td> 54.2 </td><td> 61.3 </td><td> 65.4 </td><td> 67.5 </td><td> 69.6 </td></tr>
<tr><td>Seat</td><td>Alhambra</td><td>1.4 TSI</td><td>2011</td><td> 42.8 </td><td> 52.6 </td><td> 60.5 </td><td> 63.3 </td><td> 65.9 </td><td> 68.8 </td></tr>
<tr><td>Seat</td><td>Altea</td><td>2.0 TDI</td><td>2008</td><td> 48.2 </td><td> 62.6 </td><td> 65.6 </td><td> 67.9 </td><td> 69.3 </td><td> 72.2 </td></tr>
<tr><td>Seat</td><td>Altea</td><td>2.0 TSI Freetrack</td><td>2008</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 67.4 </td><td> 68.3 </td><td> 69.6 </td></tr>
<tr><td>Seat</td><td>Altea XL</td><td>1.8 TSI</td><td>2008</td><td> 46.0 </td><td> 56.6 </td><td> 65.0 </td><td> 69.9 </td><td> 70.7 </td><td> 71.9 </td></tr>
<tr><td>Seat</td><td>Ateca</td><td>1.0</td><td>2017</td><td> 38.9 </td><td> 58.8 </td><td> 62.0 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Seat</td><td>Ateca</td><td>1.4</td><td>2017</td><td> 41.9 </td><td> 54.8 </td><td> 59.0 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Seat</td><td>Exeo</td><td>1.8</td><td>2009</td><td> 44.1 </td><td> 54.2 </td><td> 62.4 </td><td> 64.6 </td><td> 67.9 </td><td> 71.6 </td></tr>
<tr><td>Seat</td><td>Exeo</td><td>2.0 TDI Stationcar</td><td>2009</td><td> 42.2 </td><td> 51.9 </td><td> 59.7 </td><td> 64.1 </td><td> 64.9 </td><td> 66.0 </td></tr>
<tr><td>Seat</td><td>Exeo</td><td>Exeo</td><td>2009</td><td> 43.2 </td><td> 61.4 </td><td> 62.8 </td><td> 65.6 </td><td> 68.4 </td><td> 70.8 </td></tr>
<tr><td>Seat</td><td>Exeo</td><td>1.8 Stationcar</td><td>2011</td><td> 43.1 </td><td> 53.0 </td><td> 61.0 </td><td> 64.2 </td><td> 66.4 </td><td> 68.8 </td></tr>
<tr><td>Seat</td><td>Exeo</td><td>2.0 TDI Stationcar</td><td>2012</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 66.2 </td><td> 69.3 </td><td> 72.8 </td></tr>
<tr><td>Seat</td><td>Ibiza</td><td>1.4</td><td>2008</td><td> 46.4 </td><td> 57.1 </td><td> 65.7 </td><td> 68.3 </td><td> 71.5 </td><td> 75.1 </td></tr>
<tr><td>Seat</td><td>Ibiza</td><td>1.4</td><td>2010</td><td> 41.3 </td><td> 61.3 </td><td> 65.5 </td><td> 67.8 </td><td> 70.9 </td><td> 71.5 </td></tr>
<tr><td>Seat</td><td>Ibiza</td><td>1.4 TSI Cupra</td><td>2010</td><td> 45.6 </td><td> 56.2 </td><td> 64.6 </td><td> 69.2 </td><td> 70.2 </td><td> 71.6 </td></tr>
<tr><td>Seat</td><td>Ibiza</td><td>1.2 TDI</td><td>2011</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 66.1 </td><td> 68.6 </td><td> 71.5 </td></tr>
<tr><td>Seat</td><td>Ibiza</td><td>1.2 TDI Stationcar</td><td>2011</td><td> 46.4 </td><td> 63.9 </td><td> 65.4 </td><td> 67.6 </td><td> 70.7 </td><td> 72.3 </td></tr>
<tr><td>Seat</td><td>Ibiza</td><td>1.2</td><td>2012</td><td> 44.5 </td><td> 54.7 </td><td> 62.9 </td><td> 67.3 </td><td> 68.4 </td><td> 69.9 </td></tr>
<tr><td>Seat</td><td>Ibiza</td><td>1.0</td><td>2016</td><td> 39.9 </td><td> 60.8 </td><td> 63.5 </td><td> 65.8 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Seat</td><td>Ibiza</td><td>1.0</td><td>2017</td><td> 39.2 </td><td> 56.1 </td><td> 62.3 </td><td> 64.7 </td><td> 69.1 </td><td> 69.2 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>1.4 TSI</td><td>2008</td><td> 44.7 </td><td> 55.0 </td><td> 63.3 </td><td> 67.9 </td><td> 68.8 </td><td> 70.1 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>1.8 TFSI</td><td>2008</td><td> 45.5 </td><td> 56.0 </td><td> 64.4 </td><td> 68.8 </td><td> 70.0 </td><td> 71.6 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>1.9 TDI</td><td>2008</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 65.8 </td><td> 67.1 </td><td> 68.8 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>1.4 TSI</td><td>2009</td><td> 46.1 </td><td> 56.7 </td><td> 65.2 </td><td> 68.0 </td><td> 71.0 </td><td> 74.4 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>1.6 TDI</td><td>2010</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 67.4 </td><td> 68.5 </td><td> 70.0 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>1.4</td><td>2013</td><td> 38.5 </td><td> 56.2 </td><td> 63.9 </td><td> 65.2 </td><td> 68.2 </td><td> 70.4 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>1.4</td><td>2014</td><td> 37.7 </td><td> 60.2 </td><td> 64.1 </td><td> 67.4 </td><td> 69.7 </td><td> 72.0 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>1.6 TDI Stationcar</td><td>2014</td><td> 43.0 </td><td> 57.9 </td><td> 61.7 </td><td> 63.5 </td><td> 66.2 </td><td> 69.9 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>ST Cupra 280</td><td>2015</td><td> 46.9 </td><td> 60.2 </td><td> 62.6 </td><td> 65.3 </td><td> 69.5 </td><td> 72.1 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>1.0</td><td>2016</td><td> 39.2 </td><td> 54.2 </td><td> 58.6 </td><td> 62.0 </td><td> 66.7 </td><td> 68.8 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>2.0D</td><td>2016</td><td> 43.9 </td><td> 60.8 </td><td> 64.5 </td><td> 66.7 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>1.0</td><td>2017</td><td> 39.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Seat</td><td>Leon</td><td>Cupra</td><td>2017</td><td> 42.9 </td><td> 63.7 </td><td> 65.5 </td><td> 65.9 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Seat</td><td>Leon SC</td><td>1.8 TSI</td><td>2013</td><td> 39.0 </td><td> 58.0 </td><td> 62.9 </td><td> 65.0 </td><td> 67.0 </td><td> 72.0 </td></tr>
<tr><td>Seat</td><td>MII</td><td>1.0</td><td>2012</td><td> 45.8 </td><td> 57.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.5 </td><td> 74.5 </td></tr>
<tr><td>Seat</td><td>Mii</td><td>1.0</td><td>2012</td><td> 45.0 </td><td> 55.4 </td><td> 63.8 </td><td> 65.9 </td><td> 69.4 </td><td> 73.4 </td></tr>
<tr><td>Seat</td><td>Mii</td><td>1.0</td><td>2013</td><td> 42.3 </td><td> 58.2 </td><td> 66.2 </td><td> 67.3 </td><td> 70.4 </td><td> 74.3 </td></tr>
<tr><td>Seat</td><td>Mii</td><td>1.0</td><td>2014</td><td> 42.3 </td><td> 58.2 </td><td> 66.2 </td><td> 67.3 </td><td> 70.4 </td><td> 74.3 </td></tr>
<tr><td>Skoda</td><td>Citigo</td><td>1.0</td><td>2012</td><td> 45.8 </td><td> 56.4 </td><td> 64.9 </td><td> 68.1 </td><td> 70.6 </td><td> 73.5 </td></tr>
<tr><td>Skoda</td><td>Citigo</td><td>1.0</td><td>2013</td><td> 41.5 </td><td> 59.3 </td><td> 64.1 </td><td> 68.2 </td><td> 69.0 </td><td> 73.2 </td></tr>
<tr><td>Skoda</td><td>Fabia</td><td>1.4</td><td>2008</td><td> 44.3 </td><td> 61.5 </td><td> 67.3 </td><td> 68.9 </td><td> 71.8 </td><td> 74.8 </td></tr>
<tr><td>Skoda</td><td>Fabia</td><td>1.6 Stationcar</td><td>2008</td><td> 47.1 </td><td> 57.9 </td><td> 66.6 </td><td> 70.3 </td><td> 72.5 </td><td> 74.9 </td></tr>
<tr><td>Skoda</td><td>Fabia</td><td>1.2</td><td>2010</td><td> 45.4 </td><td> 55.8 </td><td> 64.2 </td><td> 67.4 </td><td> 69.9 </td><td> 72.8 </td></tr>
<tr><td>Skoda</td><td>Fabia</td><td>1.2 TDI Stationcar</td><td>2010</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 67.5 </td><td> 69.2 </td><td> 71.3 </td></tr>
<tr><td>Skoda</td><td>Fabia</td><td>1.4</td><td>2010</td><td> 41.8 </td><td> 61.4 </td><td> 66.7 </td><td> 68.9 </td><td> 72.3 </td><td> 74.5 </td></tr>
<tr><td>Skoda</td><td>Fabia</td><td>1.2 TDI</td><td>2011</td><td> 45.8 </td><td> 62.4 </td><td> 65.9 </td><td> 68.4 </td><td> 71.2 </td><td> 73.8 </td></tr>
<tr><td>Skoda</td><td>Fabia</td><td>1.2</td><td>2015</td><td> 38.5 </td><td> 57.6 </td><td> 64.9 </td><td> 66.5 </td><td> 70.1 </td><td> 71.9 </td></tr>
<tr><td>Skoda</td><td>Fabia</td><td>1.2</td><td>2016</td><td> 36.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Skoda</td><td>Kodiaq</td><td>1.4</td><td>2017</td><td> 36.3 </td><td> 53.8 </td><td> 59.7 </td><td> 63.8 </td><td> 69.3 </td><td> 69.4 </td></tr>
<tr><td>Skoda</td><td>Octavia</td><td>1.8 TSI Stationcar</td><td>2008</td><td> 45.1 </td><td> 55.5 </td><td> 63.8 </td><td> 68.7 </td><td> 69.4 </td><td> 70.5 </td></tr>
<tr><td>Skoda</td><td>Octavia</td><td>1.4 TSI Stationcar </td><td>2009</td><td> 37.7 </td><td> 57.4 </td><td> 62.5 </td><td> 66.9 </td><td> 69.0 </td><td> 70.4 </td></tr>
<tr><td>Skoda</td><td>Octavia</td><td>1.6 TDI Stationcar</td><td>2010</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 66.2 </td><td> 67.1 </td><td> 68.4 </td></tr>
<tr><td>Skoda</td><td>Octavia</td><td>1.2</td><td>2013</td><td> 42.9 </td><td> 53.6 </td><td> 59.1 </td><td> 63.1 </td><td> 66.1 </td><td> 69.6 </td></tr>
<tr><td>Skoda</td><td>Octavia</td><td>1.0</td><td>2016</td><td> 35.9 </td><td> 53.7 </td><td> 56.3 </td><td> 60.4 </td><td> 65.0 </td><td> 67.0 </td></tr>
<tr><td>Skoda</td><td>Octavia</td><td>2.0D Stationcar</td><td>2016</td><td> 42.7 </td><td> 56.9 </td><td> 60.6 </td><td> 62.5 </td><td> 67.2 </td><td> 70.7 </td></tr>
<tr><td>Skoda</td><td>Octavia</td><td>1.4 stationcar</td><td>2017</td><td> 39.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Skoda</td><td>Octavia</td><td>1.6d</td><td>2017</td><td> 43.4 </td><td> 55.1 </td><td> 60.8 </td><td> 63.6 </td><td> 69.1 </td><td> 69.2 </td></tr>
<tr><td>Skoda</td><td>Rapid</td><td>1.2</td><td>2013</td><td> 44.9 </td><td> 57.5 </td><td> 62.9 </td><td> 65.4 </td><td> 69.2 </td><td> 71.8 </td></tr>
<tr><td>Skoda</td><td>Roomster</td><td>1.4</td><td>2008</td><td> 45.6 </td><td> 56.2 </td><td> 64.6 </td><td> 67.8 </td><td> 70.3 </td><td> 73.2 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>1.8 TSI</td><td>2008</td><td> 43.2 </td><td> 53.2 </td><td> 61.2 </td><td> 64.5 </td><td> 66.6 </td><td> 68.9 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>2.0 TDI</td><td>2008</td><td> 46.4 </td><td> 60.0 </td><td> 64.0 </td><td> 66.0 </td><td> 69.1 </td><td> 71.7 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>2.0 TDI Stationcar</td><td>2010</td><td> 47.5 </td><td> 60.4 </td><td> 64.1 </td><td> 65.6 </td><td> 68.4 </td><td> 71.4 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>1.6 TDI Greenline Stationcar </td><td>2011</td><td> 49.8 </td><td> 58.8 </td><td> 63.4 </td><td> 65.8 </td><td> 68.3 </td><td> 71.7 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>1.8 TSI Stationcar</td><td>2011</td><td> 43.4 </td><td> 53.4 </td><td> 61.4 </td><td> 64.9 </td><td> 66.7 </td><td> 68.9 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>1.4</td><td>2012</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 67.2 </td><td> 68.5 </td><td> 70.2 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>1.8</td><td>2014</td><td> 40.9 </td><td> 58.8 </td><td> 62.0 </td><td> 65.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>2.0 D</td><td>2015</td><td> 46.3 </td><td> 60.3 </td><td> 62.3 </td><td> 65.4 </td><td> 67.7 </td><td> 71.2 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>2.0D</td><td>2015</td><td> 41.6 </td><td> 58.2 </td><td> 61.1 </td><td> 63.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>2.0</td><td>2017</td><td> 48.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Skoda</td><td>Superb</td><td>2.0d</td><td>2017</td><td> 45.9 </td><td> 58.8 </td><td> 62.0 </td><td> 65.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Skoda</td><td>Yeti</td><td>1.2 TSI</td><td>2010</td><td> 39.2 </td><td> 59.1 </td><td> 65.1 </td><td> 67.1 </td><td> 71.1 </td><td> 72.1 </td></tr>
<tr><td>Skoda</td><td>Yeti</td><td>1.8 TSI</td><td>2010</td><td> 44.6 </td><td> 54.9 </td><td> 63.1 </td><td> 65.6 </td><td> 68.7 </td><td> 72.2 </td></tr>
<tr><td>Skoda</td><td>Yeti</td><td>1.4 TSI</td><td>2012</td><td> 38.7 </td><td> 56.8 </td><td> 63.2 </td><td> 65.8 </td><td> 68.9 </td><td> 71.8 </td></tr>
<tr><td>Skoda</td><td>Yeti</td><td>1.2</td><td>2014</td><td> 35.9 </td><td> 54.7 </td><td> 59.5 </td><td> 62.9 </td><td> 66.9 </td><td> 70.6 </td></tr>
<tr><td>Skoda</td><td>Yeti</td><td>2.0D</td><td>2017</td><td> 49.9 </td><td> 57.8 </td><td> 62.0 </td><td> 66.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Smart</td><td>Forfour</td><td>0.9</td><td>2016</td><td> 47.9 </td><td> 62.7 </td><td> 65.5 </td><td> 68.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Smart</td><td>Fortwo</td><td>&nbsp;</td><td>2008</td><td> 49.7 </td><td> 65.3 </td><td> 71.2 </td><td> 74.5 </td><td> 77.6 </td><td> 81.1 </td></tr>
<tr><td>Smart</td><td>Fortwo</td><td>1.0</td><td>2009</td><td> 47.1 </td><td> 58.0 </td><td> 66.7 </td><td> 70.9 </td><td> 72.5 </td><td> 74.5 </td></tr>
<tr><td>Smart</td><td>Fortwo</td><td>1.0</td><td>2011</td><td> 46.7 </td><td> 57.4 </td><td> 66.1 </td><td> 70.8 </td><td> 71.8 </td><td> 73.2 </td></tr>
<tr><td>Smart</td><td>Fortwo</td><td>1.0</td><td>2013</td><td> 43.4 </td><td> 65.7 </td><td> 67.3 </td><td> 70.5 </td><td> 73.4 </td><td> 75.8 </td></tr>
<tr><td>Smart</td><td>Fortwo</td><td>&nbsp;</td><td>2015</td><td> 47.3 </td><td> 62.9 </td><td> 66.9 </td><td> 70.5 </td><td> 72.8 </td><td> 77.0 </td></tr>
<tr><td>SRT</td><td>Viper</td><td>8.4 V10</td><td>2012</td><td> 58.5 </td><td> 67.5 </td><td> 73.2 </td><td> 76.1 </td><td> 78.8 </td><td> 81.6 </td></tr>
<tr><td>SsangYong</td><td>Korando</td><td>2.0</td><td>2012</td><td> 45.1 </td><td> 55.5 </td><td> 63.8 </td><td> 68.3 </td><td> 69.4 </td><td> 70.9 </td></tr>
<tr><td>SsangYong</td><td>Tivoli</td><td>1.6</td><td>2016</td><td> 38.5 </td><td> 60.6 </td><td> 64.6 </td><td> 68.7 </td><td> 72.3 </td><td> 75.7 </td></tr>
<tr><td>Subaru</td><td>BRZ</td><td>2.0</td><td>2012</td><td> 44.8 </td><td> 56.6 </td><td> 64.0 </td><td> 67.7 </td><td> 71.5 </td><td> 75.3 </td></tr>
<tr><td>Subaru</td><td>Forester</td><td>2.0</td><td>2008</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 67.0 </td><td> 68.5 </td><td> 70.4 </td></tr>
<tr><td>Subaru</td><td>Forester</td><td>2.0D</td><td>2009</td><td> 43.6 </td><td> 53.6 </td><td> 61.6 </td><td> 65.0 </td><td> 67.1 </td><td> 69.4 </td></tr>
<tr><td>Subaru</td><td>Forester</td><td>2.5 XT</td><td>2009</td><td> 44.9 </td><td> 56.0 </td><td> 62.9 </td><td> 66.8 </td><td> 69.0 </td><td> 71.2 </td></tr>
<tr><td>Subaru</td><td>Forester</td><td>2.0 turbo</td><td>2013</td><td> 39.9 </td><td> 51.7 </td><td> 58.9 </td><td> 63.3 </td><td> 64.5 </td><td> 65.7 </td></tr>
<tr><td>Subaru</td><td>Forester</td><td>2.0D</td><td>2015</td><td> 42.0 </td><td> 61.3 </td><td> 64.2 </td><td> 66.2 </td><td> 69.1 </td><td> 71.7 </td></tr>
<tr><td>Subaru</td><td>Forester SUV</td><td>2.0</td><td>2013</td><td> 39.9 </td><td> 51.7 </td><td> 58.9 </td><td> 63.3 </td><td> 64.5 </td><td> 65.7 </td></tr>
<tr><td>Subaru</td><td>Impreza</td><td>2.0</td><td>2008</td><td> 44.7 </td><td> 55.0 </td><td> 63.3 </td><td> 66.5 </td><td> 68.9 </td><td> 71.5 </td></tr>
<tr><td>Subaru</td><td>Impreza</td><td>2.5</td><td>2008</td><td> 45.4 </td><td> 55.9 </td><td> 62.4 </td><td> 66.0 </td><td> 68.4 </td><td> 70.7 </td></tr>
<tr><td>Subaru</td><td>Impreza</td><td>WRX STI</td><td>2008</td><td> 45.7 </td><td> 56.2 </td><td> 64.7 </td><td> 69.0 </td><td> 70.3 </td><td> 72.0 </td></tr>
<tr><td>Subaru</td><td>Impreza</td><td>WRX</td><td>2011</td><td> 54.8 </td><td> 63.2 </td><td> 68.4 </td><td> 71.4 </td><td> 72.7 </td><td> 74.1 </td></tr>
<tr><td>Subaru</td><td>Impreza</td><td>WRX STI</td><td>2011</td><td> 58.3 </td><td> 65.7 </td><td> 70.3 </td><td> 72.9 </td><td> 74.4 </td><td> 76.0 </td></tr>
<tr><td>Subaru</td><td>Justy</td><td>1.0</td><td>2008</td><td> 46.2 </td><td> 56.8 </td><td> 65.3 </td><td> 68.7 </td><td> 71.1 </td><td> 73.7 </td></tr>
<tr><td>Subaru</td><td>Legacy</td><td>2.0 D</td><td>2008</td><td> 49.3 </td><td> 61.8 </td><td> 64.5 </td><td> 66.5 </td><td> 68.8 </td><td> 72.8 </td></tr>
<tr><td>Subaru</td><td>Legacy</td><td>2.0D Stationcar</td><td>2008</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 66.0 </td><td> 68.4 </td><td> 71.0 </td></tr>
<tr><td>Subaru</td><td>Legacy</td><td>2.0D Stationcar</td><td>2009</td><td> 44.5 </td><td> 54.7 </td><td> 62.9 </td><td> 65.8 </td><td> 68.5 </td><td> 71.6 </td></tr>
<tr><td>Subaru</td><td>Legacy</td><td>2.5 GT</td><td>2010</td><td> 37.4 </td><td> 48.0 </td><td> 54.6 </td><td> 58.0 </td><td> 61.0 </td><td> 64.0 </td></tr>
<tr><td>Subaru</td><td>Levorg</td><td>1.6</td><td>2016</td><td> 46.8 </td><td> 55.9 </td><td> 60.7 </td><td> 64.3 </td><td> 67.2 </td><td> 72.1 </td></tr>
<tr><td>Subaru</td><td>Levorg</td><td>1.6</td><td>2016</td><td> 40.9 </td><td> 55.5 </td><td> 60.8 </td><td> 64.3 </td><td> 68.0 </td><td> 70.1 </td></tr>
<tr><td>Subaru</td><td>Outback</td><td>2.5</td><td>2010</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 65.7 </td><td> 68.3 </td><td> 71.3 </td></tr>
<tr><td>Subaru</td><td>Outback</td><td>2.0D</td><td>2015</td><td> 42.1 </td><td> 57.6 </td><td> 63.1 </td><td> 65.6 </td><td> 68.0 </td><td> 71.1 </td></tr>
<tr><td>Subaru</td><td>Trezia</td><td>1.3</td><td>2011</td><td> 46.3 </td><td> 57.0 </td><td> 65.6 </td><td> 67.7 </td><td> 71.4 </td><td> 75.6 </td></tr>
<tr><td>Subaru</td><td>Tribeca</td><td>3.6</td><td>2008</td><td> 41.5 </td><td> 52.0 </td><td> 58.6 </td><td> 62.0 </td><td> 65.0 </td><td> 68.0 </td></tr>
<tr><td>Subaru</td><td>Tribeca</td><td>3.6</td><td>2009</td><td> 42.4 </td><td> 52.2 </td><td> 60.1 </td><td> 62.4 </td><td> 65.4 </td><td> 68.8 </td></tr>
<tr><td>Subaru</td><td>WRX</td><td>STi</td><td>2011</td><td> 46.3 </td><td> 57.0 </td><td> 65.6 </td><td> 69.7 </td><td> 71.3 </td><td> 73.3 </td></tr>
<tr><td>Subaru</td><td>WRX</td><td>2.0</td><td>2014</td><td> 45.3 </td><td> 56.4 </td><td> 63.2 </td><td> 67.1 </td><td> 68.9 </td><td> 70.6 </td></tr>
<tr><td>Subaru</td><td>WRX</td><td>STi</td><td>2014</td><td> 49.1 </td><td> 63.0 </td><td> 65.0 </td><td> 69.0 </td><td> 70.4 </td><td> 74.0 </td></tr>
<tr><td>Subaru</td><td>XV</td><td>2.0 CVT</td><td>2012</td><td> 42.5 </td><td> 55.6 </td><td> 62.6 </td><td> 67.0 </td><td> 70.2 </td><td> 73.4 </td></tr>
<tr><td>Subaru</td><td>XV</td><td>2.0</td><td>2013</td><td> 41.9 </td><td> 55.0 </td><td> 62.9 </td><td> 68.0 </td><td> 68.7 </td><td> 69.5 </td></tr>
<tr><td>Suzuki</td><td>Alto</td><td>1.0</td><td>2009</td><td> 45.8 </td><td> 56.3 </td><td> 64.8 </td><td> 68.9 </td><td> 70.4 </td><td> 72.3 </td></tr>
<tr><td>Suzuki</td><td>Alto</td><td>1.0</td><td>2013</td><td> 40.1 </td><td> 62.1 </td><td> 67.2 </td><td> 70.2 </td><td> 74.3 </td><td> 77.0 </td></tr>
<tr><td>Suzuki</td><td>Grand Vitara</td><td>2.7 V6</td><td>2008</td><td> 45.2 </td><td> 55.6 </td><td> 63.9 </td><td> 67.1 </td><td> 69.6 </td><td> 72.5 </td></tr>
<tr><td>Suzuki</td><td>Kizashi</td><td>SLS</td><td>2010</td><td> 40.7 </td><td> 53.8 </td><td> 61.9 </td><td> 66.2 </td><td> 69.8 </td><td> 73.3 </td></tr>
<tr><td>Suzuki</td><td>Kizashi</td><td>2.4</td><td>2011</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 67.9 </td><td> 68.7 </td><td> 69.9 </td></tr>
<tr><td>Suzuki</td><td>Kizashi</td><td>2.4</td><td>2011</td><td> 44.7 </td><td> 55.0 </td><td> 63.2 </td><td> 67.9 </td><td> 68.7 </td><td> 69.9 </td></tr>
<tr><td>Suzuki</td><td>S-Cross</td><td>1.0</td><td>2017</td><td> 37.9 </td><td> 58.8 </td><td> 62.5 </td><td> 66.3 </td><td> 68.2 </td><td> 71.7 </td></tr>
<tr><td>Suzuki</td><td>Splash</td><td>1.0</td><td>2008</td><td> 44.8 </td><td> 61.6 </td><td> 66.7 </td><td> 69.2 </td><td> 73.0 </td><td> 77.3 </td></tr>
<tr><td>Suzuki</td><td>Splash</td><td>1.2</td><td>2008</td><td> 38.2 </td><td> 59.4 </td><td> 65.0 </td><td> 68.5 </td><td> 70.6 </td><td> 73.5 </td></tr>
<tr><td>Suzuki</td><td>Splash</td><td>1.0</td><td>2013</td><td> 47.3 </td><td> 60.0 </td><td> 64.8 </td><td> 69.4 </td><td> 72.9 </td><td> 76.6 </td></tr>
<tr><td>Suzuki</td><td>Splash</td><td>1.0</td><td>2013</td><td> 37.9 </td><td> 60.7 </td><td> 64.2 </td><td> 69.1 </td><td> 72.2 </td><td> 74.1 </td></tr>
<tr><td>Suzuki</td><td>Swift</td><td>1.3</td><td>2010</td><td> 40.0 </td><td> 61.4 </td><td> 65.5 </td><td> 68.9 </td><td> 71.7 </td><td> 75.6 </td></tr>
<tr><td>Suzuki</td><td>Swift</td><td>1.2</td><td>2011</td><td> 46.8 </td><td> 61.1 </td><td> 66.1 </td><td> 70.1 </td><td> 72.1 </td><td> 74.1 </td></tr>
<tr><td>Suzuki</td><td>Swift</td><td>1.2</td><td>2011</td><td> 45.7 </td><td> 56.2 </td><td> 64.7 </td><td> 68.5 </td><td> 70.3 </td><td> 72.5 </td></tr>
<tr><td>Suzuki</td><td>Swift</td><td>1.6</td><td>2012</td><td> 46.2 </td><td> 56.9 </td><td> 65.4 </td><td> 69.2 </td><td> 71.1 </td><td> 73.4 </td></tr>
<tr><td>Suzuki</td><td>Swift</td><td>1.2</td><td>2017</td><td> 36.2 </td><td> 58.4 </td><td> 62.8 </td><td> 66.6 </td><td> 72.4 </td><td> 72.5 </td></tr>
<tr><td>Suzuki</td><td>SX4</td><td>1.6</td><td>2010</td><td> 45.5 </td><td> 56.0 </td><td> 64.4 </td><td> 68.6 </td><td> 70.0 </td><td> 71.8 </td></tr>
<tr><td>Suzuki</td><td>SX4</td><td>1.6</td><td>2013</td><td> 37.7 </td><td> 58.0 </td><td> 61.7 </td><td> 65.5 </td><td> 68.9 </td><td> 72.8 </td></tr>
<tr><td>Suzuki</td><td>Vitara</td><td>1.6</td><td>2015</td><td> 39.3 </td><td> 59.6 </td><td> 65.4 </td><td> 68.5 </td><td> 71.3 </td><td> 73.8 </td></tr>
<tr><td>Tesla</td><td>Model S</td><td>Hybrid</td><td>2012</td><td> 35.6 </td><td> 48.3 </td><td> 56.0 </td><td> 60.9 </td><td> 61.8 </td><td> 62.7 </td></tr>
<tr><td>Tesla</td><td>Model S</td><td>Hybrid</td><td>2013</td><td> 35.0 </td><td> 55.2 </td><td> 61.0 </td><td> 64.1 </td><td> 67.6 </td><td> 68.1 </td></tr>
<tr><td>Tesla</td><td>Model S</td><td>90D</td><td>2016</td><td> 43.2 </td><td> 51.6 </td><td> 56.2 </td><td> 59.6 </td><td> 63.6 </td><td> 66.5 </td></tr>
<tr><td>Tesla</td><td>Model X</td><td>P90D</td><td>2016</td><td> 34.4 </td><td> 53.1 </td><td> 58.1 </td><td> 61.5 </td><td> 65.2 </td><td> 67.3 </td></tr>
<tr><td>Tesla</td><td>Model X</td><td>P100D</td><td>2017</td><td> 35.9 </td><td> 53.8 </td><td> 58.5 </td><td> 63.3 </td><td> 65.2 </td><td> 68.6 </td></tr>
<tr><td>Toyota</td><td>4Runner</td><td>4.0 V6</td><td>2010</td><td> 38.6 </td><td> 50.5 </td><td> 58.0 </td><td> 61.8 </td><td> 65.4 </td><td> 69.0 </td></tr>
<tr><td>Toyota</td><td>4Runner</td><td>4.0 V6</td><td>2014</td><td> 43.5 </td><td> 51.7 </td><td> 57.0 </td><td> 59.2 </td><td> 63.0 </td><td> 66.8 </td></tr>
<tr><td>Toyota</td><td>Auris</td><td>1.3</td><td>2009</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 66.3 </td><td> 69.3 </td><td> 72.7 </td></tr>
<tr><td>Toyota</td><td>Auris</td><td>GTI180</td><td>2009</td><td> 47.8 </td><td> 60.8 </td><td> 63.8 </td><td> 68.8 </td><td> 70.9 </td><td> 73.0 </td></tr>
<tr><td>Toyota</td><td>Auris</td><td>1.6</td><td>2010</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 66.3 </td><td> 69.3 </td><td> 72.7 </td></tr>
<tr><td>Toyota</td><td>Auris</td><td>1.8</td><td>2010</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 66.9 </td><td> 69.3 </td><td> 71.9 </td></tr>
<tr><td>Toyota</td><td>Auris</td><td>Full Hybrid</td><td>2010</td><td> 45.5 </td><td> 59.1 </td><td> 65.1 </td><td> 67.1 </td><td> 70.1 </td><td> 74.1 </td></tr>
<tr><td>Toyota</td><td>Auris</td><td>1.8 Hybrid</td><td>2013</td><td> 32.9 </td><td> 54.9 </td><td> 59.9 </td><td> 62.3 </td><td> 66.7 </td><td> 70.7 </td></tr>
<tr><td>Toyota</td><td>Auris</td><td>Hybrid</td><td>2013</td><td> 45.9 </td><td> 56.5 </td><td> 60.6 </td><td> 65.3 </td><td> 67.6 </td><td> 71.3 </td></tr>
<tr><td>Toyota</td><td>Auris</td><td>1.2</td><td>2016</td><td> 37.2 </td><td> 55.1 </td><td> 60.2 </td><td> 65.1 </td><td> 68.7 </td><td> 70.8 </td></tr>
<tr><td>Toyota</td><td>Avalon</td><td>Hybrid</td><td>2012</td><td> 38.5 </td><td> 48.9 </td><td> 55.4 </td><td> 58.7 </td><td> 61.9 </td><td> 65.2 </td></tr>
<tr><td>Toyota</td><td>Avalon</td><td>2.5 Hybrid</td><td>2016</td><td> 39.4 </td><td> 50.6 </td><td> 57.4 </td><td> 61.4 </td><td> 63.2 </td><td> 65.0 </td></tr>
<tr><td>Toyota</td><td>Avensis</td><td>2.2 D-4D</td><td>2008</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 63.4 </td><td> 67.2 </td><td> 71.5 </td></tr>
<tr><td>Toyota</td><td>Avensis</td><td>1.8 Stationcar</td><td>2009</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 65.1 </td><td> 67.6 </td><td> 70.3 </td></tr>
<tr><td>Toyota</td><td>Avensis</td><td>2.2 D-4D Stationcar</td><td>2009</td><td> 52.2 </td><td> 60.3 </td><td> 65.1 </td><td> 67.2 </td><td> 70.3 </td><td> 72.2 </td></tr>
<tr><td>Toyota</td><td>Avensis</td><td>2.0 Stationcar</td><td>2010</td><td> 43.8 </td><td> 53.9 </td><td> 62.0 </td><td> 64.9 </td><td> 67.5 </td><td> 70.5 </td></tr>
<tr><td>Toyota</td><td>Avensis</td><td>2.0D</td><td>2012</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 67.3 </td><td> 69.0 </td><td> 71.1 </td></tr>
<tr><td>Toyota</td><td>Avensis</td><td>1.6D</td><td>2015</td><td> 46.7 </td><td> 58.4 </td><td> 61.6 </td><td> 65.3 </td><td> 68.7 </td><td> 72.0 </td></tr>
<tr><td>Toyota</td><td>Aygo</td><td>1.0</td><td>2008</td><td> 46.8 </td><td> 57.6 </td><td> 66.2 </td><td> 71.6 </td><td> 72.0 </td><td> 72.8 </td></tr>
<tr><td>Toyota</td><td>Aygo</td><td>1.0</td><td>2009</td><td> 46.4 </td><td> 57.1 </td><td> 65.7 </td><td> 69.9 </td><td> 71.4 </td><td> 73.3 </td></tr>
<tr><td>Toyota</td><td>Aygo</td><td>1.0</td><td>2012</td><td> 47.2 </td><td> 58.1 </td><td> 66.8 </td><td> 71.8 </td><td> 72.6 </td><td> 73.8 </td></tr>
<tr><td>Toyota</td><td>Aygo</td><td>1.0</td><td>2013</td><td> 45.5 </td><td> 62.6 </td><td> 67.9 </td><td> 71.6 </td><td> 75.0 </td><td> 78.3 </td></tr>
<tr><td>Toyota</td><td>Aygo</td><td>1.0</td><td>2014</td><td> 47.6 </td><td> 63.7 </td><td> 68.5 </td><td> 70.5 </td><td> 73.3 </td><td> 77.0 </td></tr>
<tr><td>Toyota</td><td>Camry</td><td>Hybrid</td><td>2013</td><td> 35.2 </td><td> 49.1 </td><td> 57.6 </td><td> 62.6 </td><td> 64.7 </td><td> 66.8 </td></tr>
<tr><td>Toyota</td><td>C-HR</td><td>1.2</td><td>2017</td><td> 35.9 </td><td> 58.8 </td><td> 62.5 </td><td> 66.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Toyota</td><td>C-HR</td><td>1.8</td><td>2017</td><td> 35.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Toyota</td><td>Corolla</td><td>1.6 16v VVT-I</td><td>2008</td><td> 35.6 </td><td> 60.3 </td><td> 64.0 </td><td> 67.2 </td><td> 70.0 </td><td> 71.2 </td></tr>
<tr><td>Toyota</td><td>Corolla</td><td>S</td><td>2009</td><td> 43.4 </td><td> 55.0 </td><td> 62.2 </td><td> 66.3 </td><td> 68.4 </td><td> 70.5 </td></tr>
<tr><td>Toyota</td><td>Corolla</td><td>1.8</td><td>2014</td><td> 39.2 </td><td> 52.6 </td><td> 60.8 </td><td> 65.7 </td><td> 67.5 </td><td> 69.2 </td></tr>
<tr><td>Toyota</td><td>GT86</td><td>2.0</td><td>2012</td><td> 45.8 </td><td> 56.3 </td><td> 64.8 </td><td> 66.8 </td><td> 70.5 </td><td> 74.7 </td></tr>
<tr><td>Toyota</td><td>GT86</td><td>2.0</td><td>2014</td><td> 45.5 </td><td> 63.2 </td><td> 66.6 </td><td> 69.9 </td><td> 71.5 </td><td> 73.3 </td></tr>
<tr><td>Toyota</td><td>Highlander</td><td>Hybrid</td><td>2008</td><td> 42.6 </td><td> 53.7 </td><td> 60.5 </td><td> 64.5 </td><td> 65.9 </td><td> 67.3 </td></tr>
<tr><td>Toyota</td><td>Highlander</td><td>Hybrid</td><td>2011</td><td> 38.6 </td><td> 52.3 </td><td> 60.7 </td><td> 65.5 </td><td> 67.9 </td><td> 70.3 </td></tr>
<tr><td>Toyota</td><td>Highlander</td><td>3.5 V6</td><td>2014</td><td> 40.7 </td><td> 51.5 </td><td> 58.1 </td><td> 61.8 </td><td> 63.8 </td><td> 65.9 </td></tr>
<tr><td>Toyota</td><td>iQ</td><td>1.0</td><td>2009</td><td> 45.4 </td><td> 55.8 </td><td> 64.2 </td><td> 67.9 </td><td> 69.8 </td><td> 72.1 </td></tr>
<tr><td>Toyota</td><td>IQ</td><td>1.0</td><td>2013</td><td> 43.9 </td><td> 60.3 </td><td> 65.3 </td><td> 68.9 </td><td> 71.8 </td><td> 74.3 </td></tr>
<tr><td>Toyota</td><td>Land Cruiser</td><td>V8 4.7</td><td>2008</td><td> 42.3 </td><td> 52.1 </td><td> 59.9 </td><td> 63.0 </td><td> 65.2 </td><td> 67.6 </td></tr>
<tr><td>Toyota</td><td>Land Cruiser</td><td>3.0 D-4D</td><td>2010</td><td> 43.2 </td><td> 53.1 </td><td> 61.1 </td><td> 63.1 </td><td> 66.5 </td><td> 70.3 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>1.5</td><td>2008</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 65.1 </td><td> 67.6 </td><td> 70.4 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>&nbsp;</td><td>2009</td><td> 39.9 </td><td> 54.8 </td><td> 63.7 </td><td> 69.6 </td><td> 69.9 </td><td> 70.2 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>1.8</td><td>2009</td><td> 44.9 </td><td> 55.3 </td><td> 63.6 </td><td> 66.7 </td><td> 69.2 </td><td> 72.1 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>1.8 HSD</td><td>2009</td><td> 32.4 </td><td> 59.3 </td><td> 62.5 </td><td> 66.8 </td><td> 68.5 </td><td> 73.0 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>PHV</td><td>2010</td><td> 39.6 </td><td> 54.5 </td><td> 63.5 </td><td> 69.2 </td><td> 70.2 </td><td> 71.3 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>1.8</td><td>2011</td><td> 45.0 </td><td> 55.4 </td><td> 63.8 </td><td> 66.9 </td><td> 69.4 </td><td> 72.3 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>&nbsp;</td><td>2012</td><td> 45.6 </td><td> 59.1 </td><td> 63.1 </td><td> 66.7 </td><td> 70.2 </td><td> 73.6 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>1.8</td><td>2012</td><td> 46.6 </td><td> 63.0 </td><td> 66.7 </td><td> 69.2 </td><td> 71.7 </td><td> 74.6 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>1.8</td><td>2012</td><td> 44.1 </td><td> 54.2 </td><td> 62.4 </td><td> 66.2 </td><td> 67.8 </td><td> 69.8 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>1.8 Hybrid Wagon</td><td>2012</td><td> 46.0 </td><td> 53.3 </td><td> 61.5 </td><td> 66.4 </td><td> 70.9 </td><td> 74.6 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>Plug-In</td><td>2014</td><td> 44.5 </td><td> 55.6 </td><td> 60.8 </td><td> 65.4 </td><td> 68.5 </td><td> 72.0 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>Wagon</td><td>2014</td><td> 35.5 </td><td> 51.9 </td><td> 61.7 </td><td> 68.0 </td><td> 68.9 </td><td> 69.8 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>1.8 Hybrid</td><td>2016</td><td> 34.5 </td><td> 56.8 </td><td> 61.3 </td><td> 64.2 </td><td> 68.6 </td><td> 70.6 </td></tr>
<tr><td>Toyota</td><td>Prius</td><td>Hybrid</td><td>2017</td><td> 46.9 </td><td> 58.8 </td><td> 62.5 </td><td> 66.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Toyota</td><td>RAV4</td><td>2.2 D-4D</td><td>2008</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 68.1 </td><td> 69.2 </td><td> 70.7 </td></tr>
<tr><td>Toyota</td><td>RAV4</td><td>2.0 VVT-i</td><td>2012</td><td> 39.9 </td><td> 57.2 </td><td> 63.7 </td><td> 66.7 </td><td> 71.0 </td><td> 74.5 </td></tr>
<tr><td>Toyota</td><td>RAV4</td><td>2.0</td><td>2013</td><td> 38.3 </td><td> 56.3 </td><td> 60.2 </td><td> 63.9 </td><td> 67.8 </td><td> 70.9 </td></tr>
<tr><td>Toyota</td><td>RAV4</td><td>2.5</td><td>2013</td><td> 47.0 </td><td> 56.1 </td><td> 61.7 </td><td> 64.9 </td><td> 66.4 </td><td> 68.0 </td></tr>
<tr><td>Toyota</td><td>Sequoia</td><td>5.7 V8</td><td>2008</td><td> 43.0 </td><td> 54.7 </td><td> 61.9 </td><td> 66.0 </td><td> 68.2 </td><td> 70.4 </td></tr>
<tr><td>Toyota</td><td>Sienna</td><td>3.5 V6</td><td>2011</td><td> 41.4 </td><td> 53.6 </td><td> 61.0 </td><td> 65.4 </td><td> 67.1 </td><td> 68.8 </td></tr>
<tr><td>Toyota</td><td>Tundra</td><td>4.6 V8</td><td>2016</td><td> 43.8 </td><td> 55.3 </td><td> 62.3 </td><td> 66.6 </td><td> 67.9 </td><td> 69.3 </td></tr>
<tr><td>Toyota</td><td>Urban Cruiser</td><td>1.3</td><td>2009</td><td> 44.1 </td><td> 54.2 </td><td> 62.4 </td><td> 65.3 </td><td> 67.9 </td><td> 70.9 </td></tr>
<tr><td>Toyota</td><td>Venza</td><td>2.7</td><td>2009</td><td> 42.6 </td><td> 55.9 </td><td> 64.0 </td><td> 69.1 </td><td> 70.0 </td><td> 70.9 </td></tr>
<tr><td>Toyota</td><td>Verso</td><td>1.8</td><td>2008</td><td> 44.3 </td><td> 54.6 </td><td> 62.7 </td><td> 67.0 </td><td> 68.2 </td><td> 69.8 </td></tr>
<tr><td>Toyota</td><td>Verso</td><td>1.8</td><td>2009</td><td> 45.4 </td><td> 55.9 </td><td> 64.3 </td><td> 66.8 </td><td> 70.0 </td><td> 73.6 </td></tr>
<tr><td>Toyota</td><td>Verso-S</td><td>1.3</td><td>2011</td><td> 45.6 </td><td> 56.1 </td><td> 64.5 </td><td> 67.4 </td><td> 70.2 </td><td> 73.4 </td></tr>
<tr><td>Toyota</td><td>Verso-S</td><td>1.3</td><td>2011</td><td> 45.6 </td><td> 56.1 </td><td> 64.5 </td><td> 67.4 </td><td> 70.2 </td><td> 73.4 </td></tr>
<tr><td>Toyota</td><td>Yaris</td><td>1.3</td><td>2008</td><td> 47.0 </td><td> 57.8 </td><td> 66.5 </td><td> 70.1 </td><td> 72.4 </td><td> 74.9 </td></tr>
<tr><td>Toyota</td><td>Yaris</td><td>1.3 VVT-I</td><td>2010</td><td> 39.7 </td><td> 61.3 </td><td> 66.2 </td><td> 70.0 </td><td> 71.4 </td><td> 74.6 </td></tr>
<tr><td>Toyota</td><td>Yaris</td><td>1.3</td><td>2011</td><td> 46.6 </td><td> 60.0 </td><td> 65.2 </td><td> 68.1 </td><td> 71.8 </td><td> 75.3 </td></tr>
<tr><td>Toyota</td><td>Yaris</td><td>1.3</td><td>2012</td><td> 45.2 </td><td> 55.7 </td><td> 64.0 </td><td> 67.4 </td><td> 69.7 </td><td> 72.2 </td></tr>
<tr><td>Toyota</td><td>Yaris</td><td>1.5</td><td>2012</td><td> 45.7 </td><td> 55.7 </td><td> 61.5 </td><td> 65.4 </td><td> 70.4 </td><td> 73.2 </td></tr>
<tr><td>Toyota</td><td>Yaris</td><td>1.5 Hybrid</td><td>2012</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 65.9 </td><td> 68.1 </td><td> 70.5 </td></tr>
<tr><td>Volkswagen</td><td>Amarok</td><td>2.0 TDI</td><td>2012</td><td> 47.9 </td><td> 57.3 </td><td> 61.9 </td><td> 64.6 </td><td> 68.8 </td><td> 71.0 </td></tr>
<tr><td>Volkswagen</td><td>Arteon</td><td>2.0</td><td>2017</td><td> 50.8 </td><td> 58.8 </td><td> 61.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volkswagen</td><td>Beetle</td><td>1.2</td><td>2012</td><td> 45.0 </td><td> 55.4 </td><td> 63.7 </td><td> 68.4 </td><td> 69.2 </td><td> 70.4 </td></tr>
<tr><td>Volkswagen</td><td>Caddy</td><td>1.6 TDI</td><td>2011</td><td> 45.0 </td><td> 55.4 </td><td> 63.8 </td><td> 67.2 </td><td> 69.4 </td><td> 71.8 </td></tr>
<tr><td>Volkswagen</td><td>CC</td><td>2.0 T</td><td>2009</td><td> 48.8 </td><td> 57.8 </td><td> 63.3 </td><td> 66.4 </td><td> 68.2 </td><td> 70.0 </td></tr>
<tr><td>Volkswagen</td><td>CrossPolo</td><td>1.2</td><td>2014</td><td> 41.8 </td><td> 57.8 </td><td> 62.2 </td><td> 65.3 </td><td> 68.6 </td><td> 71.7 </td></tr>
<tr><td>Volkswagen</td><td>EOS</td><td>2.0 TFSI</td><td>2008</td><td> 37.1 </td><td> 59.0 </td><td> 65.0 </td><td> 67.0 </td><td> 68.3 </td><td> 69.2 </td></tr>
<tr><td>Volkswagen</td><td>EOS</td><td>1.4 TSI</td><td>2010</td><td> 34.8 </td><td> 60.1 </td><td> 64.7 </td><td> 66.4 </td><td> 68.2 </td><td> 70.0 </td></tr>
<tr><td>Volkswagen</td><td>EOS</td><td>2.0</td><td>2011</td><td> 44.8 </td><td> 55.1 </td><td> 63.4 </td><td> 67.6 </td><td> 68.9 </td><td> 70.6 </td></tr>
<tr><td>Volkswagen</td><td>Fox</td><td>1.2</td><td>2008</td><td> 46.7 </td><td> 63.9 </td><td> 66.4 </td><td> 70.6 </td><td> 72.6 </td><td> 75.0 </td></tr>
<tr><td>Volkswagen</td><td>Fox</td><td>1.2</td><td>2009</td><td> 45.8 </td><td> 56.4 </td><td> 64.9 </td><td> 69.5 </td><td> 70.5 </td><td> 71.9 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.6 Stationcar</td><td>2008</td><td> 45.0 </td><td> 55.4 </td><td> 63.8 </td><td> 68.0 </td><td> 69.3 </td><td> 71.0 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>2.0 TDI</td><td>2008</td><td> 46.0 </td><td> 62.4 </td><td> 65.2 </td><td> 67.2 </td><td> 68.6 </td><td> 70.7 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>R32</td><td>2008</td><td> 45.5 </td><td> 57.7 </td><td> 65.2 </td><td> 69.2 </td><td> 72.4 </td><td> 75.6 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4 TSI</td><td>2009</td><td> 44.0 </td><td> 56.4 </td><td> 62.3 </td><td> 64.5 </td><td> 66.7 </td><td> 70.5 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4 TSI Plus</td><td>2009</td><td> 45.3 </td><td> 55.8 </td><td> 64.1 </td><td> 66.7 </td><td> 69.8 </td><td> 73.3 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>GTI</td><td>2009</td><td> 44.1 </td><td> 54.3 </td><td> 62.5 </td><td> 66.1 </td><td> 67.9 </td><td> 70.1 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4 TSI Stationcar</td><td>2010</td><td> 44.9 </td><td> 55.2 </td><td> 63.5 </td><td> 67.2 </td><td> 69.0 </td><td> 71.2 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.6 TDI</td><td>2010</td><td> 44.4 </td><td> 54.6 </td><td> 62.8 </td><td> 67.3 </td><td> 68.3 </td><td> 69.7 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>GTD</td><td>2010</td><td> 44.5 </td><td> 54.8 </td><td> 63.0 </td><td> 66.3 </td><td> 68.6 </td><td> 71.1 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>GTI</td><td>2010</td><td> 46.4 </td><td> 56.9 </td><td> 63.7 </td><td> 66.4 </td><td> 71.7 </td><td> 77.1 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4 Cabrio</td><td>2011</td><td> 44.3 </td><td> 54.5 </td><td> 62.7 </td><td> 67.0 </td><td> 68.1 </td><td> 69.6 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4 Convertible</td><td>2011</td><td> 44.3 </td><td> 54.5 </td><td> 62.7 </td><td> 67.0 </td><td> 68.1 </td><td> 69.6 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4 TSI</td><td>2011</td><td> 44.4 </td><td> 59.0 </td><td> 64.2 </td><td> 67.4 </td><td> 68.3 </td><td> 71.1 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4 TSI</td><td>2012</td><td> 38.9 </td><td> 56.9 </td><td> 59.2 </td><td> 62.1 </td><td> 65.2 </td><td> 67.1 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4</td><td>2013</td><td> 35.9 </td><td> 54.6 </td><td> 58.9 </td><td> 62.5 </td><td> 64.7 </td><td> 67.5 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4 Stationcar</td><td>2013</td><td> 35.9 </td><td> 56.5 </td><td> 61.2 </td><td> 65.5 </td><td> 66.9 </td><td> 70.5 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.6 D</td><td>2013</td><td> 46.1 </td><td> 57.0 </td><td> 61.1 </td><td> 63.2 </td><td> 66.2 </td><td> 70.1 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.2 Sportsvan</td><td>2014</td><td> 36.4 </td><td> 54.3 </td><td> 59.2 </td><td> 61.8 </td><td> 65.5 </td><td> 69.4 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4 Sportsvan</td><td>2014</td><td> 44.3 </td><td> 58.2 </td><td> 62.2 </td><td> 65.5 </td><td> 68.3 </td><td> 70.2 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.6</td><td>2014</td><td> 42.6 </td><td> 56.1 </td><td> 59.6 </td><td> 62.3 </td><td> 65.6 </td><td> 68.6 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>GTD</td><td>2014</td><td> 43.6 </td><td> 59.2 </td><td> 63.1 </td><td> 66.9 </td><td> 68.6 </td><td> 70.3 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>GTE</td><td>2014</td><td> 42.3 </td><td> 58.2 </td><td> 61.6 </td><td> 64.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>GTI</td><td>2014</td><td> 43.6 </td><td> 60.2 </td><td> 63.6 </td><td> 66.9 </td><td> 67.6 </td><td> 69.3 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>R</td><td>2014</td><td> 35.8 </td><td> 59.1 </td><td> 62.1 </td><td> 65.1 </td><td> 69.1 </td><td> 70.5 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.4</td><td>2015</td><td> 38.2 </td><td> 57.1 </td><td> 61.1 </td><td> 63.1 </td><td> 66.0 </td><td> 69.0 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.8</td><td>2015</td><td> 42.2 </td><td> 52.5 </td><td> 58.8 </td><td> 62.5 </td><td> 64.0 </td><td> 65.5 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td> 1.0</td><td>2016</td><td> 37.9 </td><td> 56.8 </td><td> 60.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.0</td><td>2016</td><td> 39.9 </td><td> 56.8 </td><td> 59.5 </td><td> 62.2 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.0 Sportsvan</td><td>2016</td><td> 37.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>2.0D</td><td>2016</td><td> 44.9 </td><td> 58.8 </td><td> 62.0 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>GTI</td><td>2016</td><td> 43.1 </td><td> 60.2 </td><td> 63.3 </td><td> 65.6 </td><td> 66.3 </td><td> 69.7 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.0</td><td>2017</td><td> 37.7 </td><td> 55.1 </td><td> 61.0 </td><td> 65.1 </td><td> 70.2 </td><td> 70.3 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.5</td><td>2017</td><td> 37.9 </td><td> 58.8 </td><td> 61.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>1.5 stationcar</td><td>2017</td><td> 38.9 </td><td> 59.8 </td><td> 63.0 </td><td> 66.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Volkswagen</td><td>Golf</td><td>EV</td><td>2017</td><td> 43.9 </td><td> 52.3 </td><td> 57.8 </td><td> 60.5 </td><td> 67.6 </td><td> 67.7 </td></tr>
<tr><td>Volkswagen</td><td>Jetta</td><td>1.6</td><td>2008</td><td> 41.8 </td><td> 61.7 </td><td> 65.4 </td><td> 68.0 </td><td> 70.4 </td><td> 71.0 </td></tr>
<tr><td>Volkswagen</td><td>Jetta</td><td>2.0 TDI</td><td>2009</td><td> 47.8 </td><td> 58.9 </td><td> 65.5 </td><td> 69.7 </td><td> 70.6 </td><td> 71.4 </td></tr>
<tr><td>Volkswagen</td><td>Jetta</td><td>1.2</td><td>2011</td><td> 42.7 </td><td> 52.6 </td><td> 60.4 </td><td> 63.6 </td><td> 65.8 </td><td> 68.2 </td></tr>
<tr><td>Volkswagen</td><td>Jetta</td><td>1.2 TSI</td><td>2011</td><td> 43.6 </td><td> 53.1 </td><td> 58.6 </td><td> 64.1 </td><td> 67.2 </td><td> 69.6 </td></tr>
<tr><td>Volkswagen</td><td>Jetta</td><td>2.5 V5</td><td>2011</td><td> 39.8 </td><td> 50.7 </td><td> 57.4 </td><td> 61.1 </td><td> 63.5 </td><td> 66.0 </td></tr>
<tr><td>Volkswagen</td><td>Jetta</td><td>1.4 Hybrid</td><td>2013</td><td> 34.2 </td><td> 53.9 </td><td> 58.5 </td><td> 62.3 </td><td> 64.5 </td><td> 67.7 </td></tr>
<tr><td>Volkswagen</td><td>Jetta</td><td>1.4 Hybrid</td><td>2014</td><td> 35.0 </td><td> 49.8 </td><td> 58.8 </td><td> 64.4 </td><td> 65.6 </td><td> 66.8 </td></tr>
<tr><td>Volkswagen</td><td>Jetta</td><td>1.4</td><td>2016</td><td> 40.3 </td><td> 52.5 </td><td> 60.0 </td><td> 64.5 </td><td> 66.0 </td><td> 67.5 </td></tr>
<tr><td>Volkswagen</td><td>Multivan</td><td>2.0 TDI</td><td>2011</td><td> 48.7 </td><td> 60.3 </td><td> 64.3 </td><td> 68.2 </td><td> 70.5 </td><td> 73.0 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>1.8 TFSI Stationcar</td><td>2008</td><td> 43.1 </td><td> 62.0 </td><td> 64.5 </td><td> 66.5 </td><td> 68.0 </td><td> 69.5 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>1.9 TDI</td><td>2008</td><td> 44.5 </td><td> 54.7 </td><td> 62.9 </td><td> 68.0 </td><td> 68.4 </td><td> 69.1 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>2.0 TFSI Stationcar</td><td>2008</td><td> 43.6 </td><td> 53.7 </td><td> 61.7 </td><td> 66.2 </td><td> 67.1 </td><td> 68.4 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>3.6 V6 CC</td><td>2008</td><td> 41.1 </td><td> 58.8 </td><td> 61.0 </td><td> 63.5 </td><td> 66.0 </td><td> 69.7 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>2.0 TDI Stationcar</td><td>2009</td><td> 43.5 </td><td> 53.5 </td><td> 61.5 </td><td> 66.1 </td><td> 66.9 </td><td> 68.0 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>1.4 TSI</td><td>2011</td><td> 35.8 </td><td> 54.6 </td><td> 58.3 </td><td> 62.4 </td><td> 65.1 </td><td> 68.3 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>1.4 TSI</td><td>2011</td><td> 44.5 </td><td> 54.7 </td><td> 62.9 </td><td> 67.0 </td><td> 68.4 </td><td> 70.2 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>1.6 TDI</td><td>2011</td><td> 42.0 </td><td> 51.7 </td><td> 59.4 </td><td> 62.7 </td><td> 64.6 </td><td> 66.9 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>1.6 TDI Stationcar</td><td>2011</td><td> 48.5 </td><td> 58.1 </td><td> 61.4 </td><td> 64.2 </td><td> 66.9 </td><td> 69.8 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>3.5 V6</td><td>2012</td><td> 43.3 </td><td> 56.1 </td><td> 63.8 </td><td> 68.5 </td><td> 69.9 </td><td> 71.4 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>2.0 TDI</td><td>2013</td><td> 45.0 </td><td> 54.1 </td><td> 59.6 </td><td> 62.8 </td><td> 64.2 </td><td> 65.6 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>1.4</td><td>2014</td><td> 37.1 </td><td> 58.2 </td><td> 61.2 </td><td> 64.3 </td><td> 67.3 </td><td> 70.7 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>2.0 TDI</td><td>2014</td><td> 41.0 </td><td> 56.2 </td><td> 59.6 </td><td> 62.9 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>1.6 TDI Stationcar</td><td>2015</td><td> 49.7 </td><td> 58.8 </td><td> 61.6 </td><td> 64.4 </td><td> 66.2 </td><td> 69.3 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>2.0 TDI Stationcar</td><td>2015</td><td> 42.3 </td><td> 56.2 </td><td> 60.6 </td><td> 64.9 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>Volkswagen</td><td>Passat</td><td>2.0 TDI</td><td>2016</td><td> 44.9 </td><td> 59.8 </td><td> 62.5 </td><td> 65.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volkswagen</td><td>Passat CC</td><td>1.8 TSI</td><td>2008</td><td> 44.1 </td><td> 54.2 </td><td> 62.4 </td><td> 66.5 </td><td> 67.8 </td><td> 69.5 </td></tr>
<tr><td>Volkswagen</td><td>Phaeton</td><td>4.2 V8</td><td>2008</td><td> 42.9 </td><td> 52.8 </td><td> 60.7 </td><td> 63.1 </td><td> 66.1 </td><td> 69.5 </td></tr>
<tr><td>Volkswagen</td><td>Phaeton</td><td>4.2 V8 L</td><td>2010</td><td> 44.5 </td><td> 55.4 </td><td> 59.8 </td><td> 62.1 </td><td> 63.7 </td><td> 66.9 </td></tr>
<tr><td>Volkswagen</td><td>Phaeton</td><td>3.0 TDI</td><td>2011</td><td> 41.3 </td><td> 50.9 </td><td> 58.5 </td><td> 61.4 </td><td> 63.7 </td><td> 66.2 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>1.4</td><td>2009</td><td> 43.9 </td><td> 54.1 </td><td> 62.2 </td><td> 66.4 </td><td> 67.6 </td><td> 69.2 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>1.4 16V</td><td>2009</td><td> 43.1 </td><td> 61.2 </td><td> 64.4 </td><td> 67.1 </td><td> 69.4 </td><td> 71.4 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>1.2 TDI</td><td>2010</td><td> 47.9 </td><td> 60.4 </td><td> 64.1 </td><td> 66.4 </td><td> 69.5 </td><td> 71.3 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>1.2 TDI</td><td>2011</td><td> 49.5 </td><td> 61.5 </td><td> 65.1 </td><td> 68.8 </td><td> 69.3 </td><td> 71.6 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>1.2</td><td>2012</td><td> 44.8 </td><td> 55.1 </td><td> 63.4 </td><td> 67.8 </td><td> 68.9 </td><td> 70.4 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>1.2 TSI</td><td>2012</td><td> 42.2 </td><td> 58.3 </td><td> 62.6 </td><td> 65.8 </td><td> 69.1 </td><td> 72.4 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>1.4</td><td>2013</td><td> 44.7 </td><td> 58.8 </td><td> 64.6 </td><td> 65.4 </td><td> 68.8 </td><td> 71.4 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>1.0</td><td>2016</td><td> 42.1 </td><td> 62.2 </td><td> 64.3 </td><td> 66.3 </td><td> 69.2 </td><td> 72.8 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>GTI</td><td>2016</td><td> 43.9 </td><td> 61.8 </td><td> 65.5 </td><td> 69.3 </td><td> 70.1 </td><td> 73.7 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>1.0</td><td>2017</td><td> 38.9 </td><td> 57.8 </td><td> 61.0 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volkswagen</td><td>Polo</td><td>1.2</td><td>2017</td><td> 46.5 </td><td> 56.8 </td><td> 61.2 </td><td> 65.7 </td><td> 71.7 </td><td> 71.8 </td></tr>
<tr><td>Volkswagen</td><td>Scirocco</td><td>2.0 TSI</td><td>2008</td><td> 44.4 </td><td> 63.0 </td><td> 68.1 </td><td> 69.5 </td><td> 71.4 </td><td> 73.5 </td></tr>
<tr><td>Volkswagen</td><td>Scirocco</td><td>2.0 TDI</td><td>2009</td><td> 45.4 </td><td> 55.9 </td><td> 64.3 </td><td> 68.6 </td><td> 69.9 </td><td> 71.6 </td></tr>
<tr><td>Volkswagen</td><td>Scirocco</td><td>1.4 TSI</td><td>2012</td><td> 46.2 </td><td> 61.6 </td><td> 65.6 </td><td> 66.9 </td><td> 71.1 </td><td> 72.8 </td></tr>
<tr><td>Volkswagen</td><td>Scirocco</td><td>2.0 TDI</td><td>2014</td><td> 44.9 </td><td> 60.2 </td><td> 64.6 </td><td> 68.9 </td><td> 71.5 </td><td> 73.3 </td></tr>
<tr><td>Volkswagen</td><td>Sharan</td><td>2.0 TDI</td><td>2011</td><td> 46.2 </td><td> 60.5 </td><td> 61.8 </td><td> 65.3 </td><td> 67.2 </td><td> 70.8 </td></tr>
<tr><td>Volkswagen</td><td>Sharan</td><td>1.4</td><td>2012</td><td> 42.6 </td><td> 52.4 </td><td> 60.3 </td><td> 63.1 </td><td> 65.6 </td><td> 68.3 </td></tr>
<tr><td>Volkswagen</td><td>Tiguan</td><td>2.0 TDI</td><td>2008</td><td> 47.5 </td><td> 60.1 </td><td> 63.4 </td><td> 65.7 </td><td> 67.4 </td><td> 71.1 </td></tr>
<tr><td>Volkswagen</td><td>Tiguan</td><td>2.0 TFSI</td><td>2009</td><td> 45.4 </td><td> 55.8 </td><td> 64.2 </td><td> 68.3 </td><td> 69.8 </td><td> 71.7 </td></tr>
<tr><td>Volkswagen</td><td>Tiguan</td><td>2.0 TDI 4-Motion</td><td>2011</td><td> 43.8 </td><td> 58.1 </td><td> 62.1 </td><td> 64.1 </td><td> 67.4 </td><td> 70.6 </td></tr>
<tr><td>Volkswagen</td><td>Tiguan</td><td>2.0 TSI</td><td>2011</td><td> 43.0 </td><td> 53.0 </td><td> 60.9 </td><td> 63.8 </td><td> 66.3 </td><td> 69.1 </td></tr>
<tr><td>Volkswagen</td><td>Tiguan</td><td>1.4 TSI</td><td>2012</td><td> 39.4 </td><td> 55.0 </td><td> 59.8 </td><td> 63.2 </td><td> 65.6 </td><td> 69.9 </td></tr>
<tr><td>Volkswagen</td><td>Tiguan</td><td>1.4</td><td>2016</td><td> 43.9 </td><td> 54.6 </td><td> 58.6 </td><td> 60.5 </td><td> 65.6 </td><td> 67.6 </td></tr>
<tr><td>Volkswagen</td><td>Tiguan</td><td>2.0</td><td>2016</td><td> 37.9 </td><td> 55.8 </td><td> 59.0 </td><td> 62.2 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Volkswagen</td><td>Tiguan</td><td>1.4</td><td>2017</td><td> 42.9 </td><td> 57.8 </td><td> 61.5 </td><td> 65.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Volkswagen</td><td>Touareg</td><td>V8</td><td>2008</td><td> 42.9 </td><td> 53.7 </td><td> 60.3 </td><td> 64.0 </td><td> 66.1 </td><td> 68.2 </td></tr>
<tr><td>Volkswagen</td><td>Touareg</td><td>3.0 V6 TDI</td><td>2010</td><td> 43.1 </td><td> 53.0 </td><td> 61.0 </td><td> 64.7 </td><td> 66.3 </td><td> 68.3 </td></tr>
<tr><td>Volkswagen</td><td>Touareg</td><td>3.0 V6 TDI</td><td>2014</td><td> 41.0 </td><td> 56.2 </td><td> 59.6 </td><td> 62.9 </td><td> 65.7 </td><td> 67.3 </td></tr>
<tr><td>Volkswagen</td><td>Touareg</td><td>3.0 V6</td><td>2015</td><td> 41.0 </td><td> 57.2 </td><td> 60.1 </td><td> 62.9 </td><td> 66.6 </td><td> 68.3 </td></tr>
<tr><td>Volkswagen</td><td>Up</td><td>1.0</td><td>2012</td><td> 45.6 </td><td> 61.6 </td><td> 61.8 </td><td> 66.5 </td><td> 70.2 </td><td> 73.2 </td></tr>
<tr><td>Volkswagen</td><td>Up</td><td>1.0</td><td>2013</td><td> 41.7 </td><td> 58.7 </td><td> 62.8 </td><td> 66.9 </td><td> 69.4 </td><td> 73.8 </td></tr>
<tr><td>Volkswagen</td><td>Up</td><td>1.0</td><td>2014</td><td> 46.8 </td><td> 62.4 </td><td> 67.5 </td><td> 70.0 </td><td> 72.0 </td><td> 75.2 </td></tr>
<tr><td>Volkswagen</td><td>Up</td><td>1.0</td><td>2016</td><td> 43.9 </td><td> 60.8 </td><td> 64.0 </td><td> 67.3 </td><td> 69.1 </td><td> 72.7 </td></tr>
<tr><td>Volkswagen</td><td>XL1</td><td>&nbsp;</td><td>2014</td><td> 47.0 </td><td> 63.1 </td><td> 68.9 </td><td> 71.3 </td><td> 72.3 </td><td> 76.0 </td></tr>
<tr><td>Volvo</td><td>C30</td><td>2.4i</td><td>2008</td><td> 44.6 </td><td> 54.9 </td><td> 63.1 </td><td> 66.4 </td><td> 68.7 </td><td> 71.2 </td></tr>
<tr><td>Volvo</td><td>C30</td><td>2.5</td><td>2008</td><td> 44.7 </td><td> 56.0 </td><td> 62.8 </td><td> 67.0 </td><td> 68.3 </td><td> 69.6 </td></tr>
<tr><td>Volvo</td><td>C30</td><td>T5</td><td>2008</td><td> 45.1 </td><td> 61.6 </td><td> 66.1 </td><td> 68.1 </td><td> 70.0 </td><td> 72.1 </td></tr>
<tr><td>Volvo</td><td>C70</td><td>T5</td><td>2010</td><td> 44.4 </td><td> 60.6 </td><td> 64.4 </td><td> 67.8 </td><td> 70.1 </td><td> 72.3 </td></tr>
<tr><td>Volvo</td><td>D6</td><td>2.4</td><td>2015</td><td> 43.6 </td><td> 53.0 </td><td> 56.9 </td><td> 62.2 </td><td> 65.7 </td><td> 68.8 </td></tr>
<tr><td>Volvo</td><td>S40</td><td>2.0</td><td>2008</td><td> 43.2 </td><td> 53.1 </td><td> 61.1 </td><td> 65.1 </td><td> 66.4 </td><td> 68.1 </td></tr>
<tr><td>Volvo</td><td>S40</td><td>2.0</td><td>2009</td><td> 45.7 </td><td> 56.2 </td><td> 64.7 </td><td> 65.2 </td><td> 70.4 </td><td> 76.3 </td></tr>
<tr><td>Volvo</td><td>S60</td><td>2.0T</td><td>2010</td><td> 45.2 </td><td> 55.7 </td><td> 64.0 </td><td> 64.4 </td><td> 69.7 </td><td> 75.7 </td></tr>
<tr><td>Volvo</td><td>S60</td><td>D5 2.4</td><td>2011</td><td> 43.2 </td><td> 53.2 </td><td> 61.2 </td><td> 64.1 </td><td> 66.6 </td><td> 69.3 </td></tr>
<tr><td>Volvo</td><td>S60</td><td>T6</td><td>2011</td><td> 38.1 </td><td> 55.4 </td><td> 66.2 </td><td> 71.7 </td><td> 76.7 </td><td> 81.8 </td></tr>
<tr><td>Volvo</td><td>S60</td><td>T5 2.0</td><td>2012</td><td> 43.2 </td><td> 53.1 </td><td> 61.1 </td><td> 63.7 </td><td> 66.5 </td><td> 69.7 </td></tr>
<tr><td>Volvo</td><td>S60</td><td>D4</td><td>2014</td><td> 44.2 </td><td> 57.0 </td><td> 59.5 </td><td> 62.3 </td><td> 65.0 </td><td> 68.6 </td></tr>
<tr><td>Volvo</td><td>S80</td><td>&nbsp;</td><td>2008</td><td> 40.1 </td><td> 57.5 </td><td> 61.0 </td><td> 64.0 </td><td> 66.0 </td><td> 70.0 </td></tr>
<tr><td>Volvo</td><td>S80</td><td>2.0</td><td>2008</td><td> 44.3 </td><td> 54.5 </td><td> 62.7 </td><td> 66.8 </td><td> 68.1 </td><td> 69.8 </td></tr>
<tr><td>Volvo</td><td>S80</td><td>T6</td><td>2008</td><td> 42.8 </td><td> 52.6 </td><td> 60.5 </td><td> 64.4 </td><td> 65.8 </td><td> 67.6 </td></tr>
<tr><td>Volvo</td><td>S80</td><td>D5 2.4</td><td>2012</td><td> 42.8 </td><td> 52.7 </td><td> 60.6 </td><td> 63.9 </td><td> 66.0 </td><td> 68.3 </td></tr>
<tr><td>Volvo</td><td>S80</td><td>D4</td><td>2014</td><td> 43.5 </td><td> 52.7 </td><td> 56.4 </td><td> 60.6 </td><td> 64.3 </td><td> 67.2 </td></tr>
<tr><td>Volvo</td><td>S90</td><td>D4</td><td>2016</td><td> 45.9 </td><td> 57.8 </td><td> 61.0 </td><td> 63.3 </td><td> 64.3 </td><td> 67.6 </td></tr>
<tr><td>Volvo</td><td>S90</td><td>D4</td><td>2017</td><td> 44.9 </td><td> 56.8 </td><td> 60.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volvo</td><td>V40</td><td>D2</td><td>2012</td><td> 43.4 </td><td> 54.3 </td><td> 58.4 </td><td> 61.2 </td><td> 64.7 </td><td> 68.9 </td></tr>
<tr><td>Volvo</td><td>V40</td><td>T3</td><td>2012</td><td> 42.5 </td><td> 54.8 </td><td> 60.6 </td><td> 63.8 </td><td> 66.2 </td><td> 68.1 </td></tr>
<tr><td>Volvo</td><td>V40</td><td>T3 1.6</td><td>2012</td><td> 43.0 </td><td> 52.9 </td><td> 60.8 </td><td> 65.4 </td><td> 66.1 </td><td> 67.1 </td></tr>
<tr><td>Volvo</td><td>V40</td><td>D2 1.6</td><td>2013</td><td> 49.7 </td><td> 57.0 </td><td> 61.9 </td><td> 65.2 </td><td> 67.4 </td><td> 71.1 </td></tr>
<tr><td>Volvo</td><td>V40</td><td>T4 Cross Country</td><td>2014</td><td> 39.7 </td><td> 58.6 </td><td> 62.2 </td><td> 65.5 </td><td> 68.3 </td><td> 70.8 </td></tr>
<tr><td>Volvo</td><td>V50</td><td>2.0I</td><td>2008</td><td> 43.5 </td><td> 62.2 </td><td> 65.4 </td><td> 67.6 </td><td> 68.9 </td><td> 71.4 </td></tr>
<tr><td>Volvo</td><td>V50</td><td>1.6D</td><td>2010</td><td> 44.2 </td><td> 54.4 </td><td> 62.6 </td><td> 66.4 </td><td> 68.0 </td><td> 70.0 </td></tr>
<tr><td>Volvo</td><td>V60</td><td>D3 2.0</td><td>2011</td><td> 44.5 </td><td> 54.7 </td><td> 62.9 </td><td> 65.5 </td><td> 68.5 </td><td> 71.9 </td></tr>
<tr><td>Volvo</td><td>V60</td><td>D3</td><td>2012</td><td> 48.2 </td><td> 57.5 </td><td> 60.8 </td><td> 62.4 </td><td> 67.5 </td><td> 71.4 </td></tr>
<tr><td>Volvo</td><td>V60</td><td>T6 3.0</td><td>2012</td><td> 43.9 </td><td> 54.0 </td><td> 62.1 </td><td> 66.0 </td><td> 67.5 </td><td> 69.4 </td></tr>
<tr><td>Volvo</td><td>V60</td><td>D2</td><td>2015</td><td> 46.7 </td><td> 56.7 </td><td> 62.4 </td><td> 65.1 </td><td> 68.9 </td><td> 71.9 </td></tr>
<tr><td>Volvo</td><td>V70</td><td>2.4D</td><td>2008</td><td> 43.7 </td><td> 53.8 </td><td> 61.9 </td><td> 64.9 </td><td> 67.4 </td><td> 70.2 </td></tr>
<tr><td>Volvo</td><td>V70</td><td>3.2</td><td>2008</td><td> 43.9 </td><td> 54.1 </td><td> 62.2 </td><td> 64.9 </td><td> 67.7 </td><td> 70.9 </td></tr>
<tr><td>Volvo</td><td>V70</td><td>1.6D Drive</td><td>2010</td><td> 46.0 </td><td> 58.8 </td><td> 61.9 </td><td> 64.3 </td><td> 66.4 </td><td> 70.4 </td></tr>
<tr><td>Volvo</td><td>V90</td><td>T5 Stationcar</td><td>2016</td><td> 46.2 </td><td> 53.8 </td><td> 60.8 </td><td> 63.8 </td><td> 67.4 </td><td> 69.5 </td></tr>
<tr><td>Volvo</td><td>V90</td><td>D5 stationcar</td><td>2017</td><td> 39.9 </td><td> 57.8 </td><td> 62.0 </td><td> 64.5 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volvo</td><td>V90</td><td>T5 stationcar</td><td>2017</td><td> 44.6 </td><td> 52.0 </td><td> 57.3 </td><td> 61.2 </td><td> 67.3 </td><td> 67.4 </td></tr>
<tr><td>Volvo</td><td>XC60</td><td>D5 Geartronic</td><td>2008</td><td> 45.4 </td><td> 54.8 </td><td> 60.5 </td><td> 63.5 </td><td> 67.0 </td><td> 69.3 </td></tr>
<tr><td>Volvo</td><td>XC60</td><td>T6</td><td>2009</td><td> 45.4 </td><td> 55.8 </td><td> 64.2 </td><td> 67.4 </td><td> 69.9 </td><td> 72.8 </td></tr>
<tr><td>Volvo</td><td>XC60</td><td>2.4D</td><td>2010</td><td> 42.7 </td><td> 52.6 </td><td> 60.4 </td><td> 63.0 </td><td> 65.8 </td><td> 69.0 </td></tr>
<tr><td>Volvo</td><td>XC60</td><td>T6</td><td>2010</td><td> 43.3 </td><td> 54.7 </td><td> 61.8 </td><td> 65.5 </td><td> 68.6 </td><td> 71.7 </td></tr>
<tr><td>Volvo</td><td>XC60</td><td>D5 2.4</td><td>2011</td><td> 43.6 </td><td> 53.6 </td><td> 61.6 </td><td> 65.8 </td><td> 67.0 </td><td> 68.6 </td></tr>
<tr><td>Volvo</td><td>XC60</td><td>D4</td><td>2015</td><td> 48.9 </td><td> 55.4 </td><td> 58.7 </td><td> 61.6 </td><td> 64.6 </td><td> 67.7 </td></tr>
<tr><td>Volvo</td><td>XC60</td><td>2.4D</td><td>2016</td><td> 43.9 </td><td> 56.8 </td><td> 60.0 </td><td> 63.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volvo</td><td>XC60</td><td>D5</td><td>2016</td><td> 46.8 </td><td> 55.6 </td><td> 60.1 </td><td> 62.8 </td><td> 67.1 </td><td> 69.8 </td></tr>
<tr><td>Volvo</td><td>XC60</td><td>2.0d</td><td>2017</td><td> 43.6 </td><td> 51.6 </td><td> 56.1 </td><td> 60.6 </td><td> 67.1 </td><td> 67.2 </td></tr>
<tr><td>Volvo</td><td>XC70</td><td>D5</td><td>2008</td><td> 43.2 </td><td> 53.2 </td><td> 61.2 </td><td> 65.5 </td><td> 66.5 </td><td> 67.9 </td></tr>
<tr><td>Volvo</td><td>XC90</td><td>D5</td><td>2015</td><td> 44.1 </td><td> 55.8 </td><td> 61.5 </td><td> 64.2 </td><td> 67.9 </td><td> 70.0 </td></tr>
<tr><td>Volvo</td><td>XC90</td><td>D4</td><td>2016</td><td> 42.9 </td><td> 56.8 </td><td> 60.5 </td><td> 64.3 </td><td> 66.2 </td><td> 69.6 </td></tr>
<tr><td>Volvo</td><td>XC90</td><td>T8 Twin Engine</td><td>2016</td><td> 37.3 </td><td> 50.3 </td><td> 56.6 </td><td> 60.9 </td><td> 65.4 </td><td> 67.8 </td></tr>
<tr><td>Volvo</td><td>XC90</td><td>2.0d</td><td>2017</td><td> 47.9 </td><td> 64.7 </td><td> 65.5 </td><td> 66.3 </td><td> 67.2 </td><td> 70.6 </td></tr>
<tr><td>Volvo</td><td>XC90</td><td>T6</td><td>2017</td><td> 39.9 </td><td> 55.8 </td><td> 60.0 </td><td> 64.3 </td><td> 65.2 </td><td> 68.6 </td>
</tr>
</tbody>
</table>
  '''
soup = BeautifulSoup(html_string, 'lxml')  # Parse the HTML as a string

table = soup.find_all('table')[0]  # Grab the first table

new_table = pd.DataFrame(columns=range(0, 10), index=[0])  # I know the size

row_marker = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        new_table.iat[row_marker, column_marker] = column.get_text()
        column_marker += 1

print(new_table)