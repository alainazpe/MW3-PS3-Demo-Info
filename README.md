# MW3-PS3-Demo-Info
Script that reads a folder with PS3 MW3 theater gameplays and prints the unprotected info in html table format.

DISCLAIMER: THIS SCRIPT CAN PRINT UNPROTECTED PARTS OF THE CONSOLE GAME THEATER FILES. IT IS NOT DESIGNED FOR GAME CHEATING. IT IS NOT MADE FOR BREAKING GAME PROTECTIONS AS GAME EULAs TERMS APPLY. NO GAME FILES/ASSETS ARE INCLUDED WITH THIS TOOL. 

# Usage:

Add example file to a Folder named Demo on C Drive.

Then run this command:

    python scriptCine.py C:/Demo

Printed example:
```
<table><thead><th>Fichero</th><th>Modo</th><th>Mapa</th><th>Jugador</th><th>Fecha</th></thead><tbody>
<tr><td> file1.dat </td> <td>dm</td><td>pm_game1</td><td>player1</td><td>17/01/2000 20:36:32</td></tr>
<tr><td> file2.dat </td> <td>dm</td><td>pm_game3</td><td>player1</td><td>22/02/2003 22:38:38</td></tr>
<tr><td> file3.dat </td> <td>dm</td><td>pm_game2</td><td>player1</td><td>12/03/2002 14:56:49</td></tr>
<tr><td> file4.dat </td> <td>dm</td><td>pm_game4</td><td>player1</td><td>11/04/2006 23:24:52</td></tr>
</tbody></table>
```
Which can be represented in a web browser:

<img width="487" height="156" alt="image" src="https://github.com/user-attachments/assets/a120f200-a828-4be9-8f51-05ad9fbae1e3" />


  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
