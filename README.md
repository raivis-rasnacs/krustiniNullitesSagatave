## Krustiņi un nullītes konsolē
Tavs uzdevums ir atvērt doto failu *tictactoe.py* un tajā iedziļināties, lai izprastu spēles darbību. Pievērs uzmanību komentāriem pirms katras funkcijas!<br>
Koda sākumā ir pievienota random bibliotēka, kas tiek izmantota spēles algoritmā.<br>
Ir nodefinēts arī saraksts ar nosaukumu *laukums*, kurā vērtības mainīsies spēles gaitā.<br>

Spēles algoritms ir sadalīts 5 loģiskās funkcijās, no kurām 2 ir jau uzrakstītas:
* jaunaSpele() - nodzēš esošās saraksta vērtības un sanumurē ar 1 - 9 jaunai spēlei
* spelesBeigas() - jautā spēlētājam, vai turpinās spēli. Ja turpinās, tad izsauc jaunaSpele()

Tavs uzdevums būs pabeigt pārējās 3 funkcijas.

Funkcija *ziiimeeLaukumu()* paredzēta grafiska spēles laukuma atveidošanai konsolē (terminālī). Tev jāizveido cikls, kas caurskata doto sarakstu un izdrukā to konsolē atbilstoši nosacījumiem komentārā. Tev noderēs parametrs *end=* funkcijai print().

Funkcija *gajiens()* jāpapildina ar gājiena izdarīšanas algoritmu, kur spēlētājam jāievada skaitlis 1 - 9 un sarakstā attiecīgais elements tiek aizstāts ar X vai 0.<br>

Funkcijā *parbaudaUzvaru()* jāsastāda algoritms, kurš pārbauda, vai laukumā jau neeksistē kāda uzvaroša kombinācija, piemēram, 1-5-9 vai 4-5-6 utml. Šeit iespējami dažādi realizācijas varianti - gan ar ciklu, gan bez tā.
Atgriežāmās vērtības ir dotas komentārā.

Ja rodas grūtības, ieskaties [šeit](https://prog.kmu.lv/programmesana/python/2d_saraksti/) un aplūko piemēru par kuģu spēli!
