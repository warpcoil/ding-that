# DingThats fonts v1.000

Three free, open-source dingbat fonts from [dingthat.com](https://dingthat.com).

| Font | What's in it | Glyphs |
|---|---|---|
| **DingThats GUI** | Box drawing (single, double, mixed, rounded), shade blocks, classic PC symbols, GUI widgets. Monospaced; box characters tile seamlessly. | 111 |
| **DingThats Shapes** | Arrows, triangles, squares, circles, stars, checks, crosses, media controls and UI symbols. | 94 |
| **DingThats Objects** | Buildings, vehicles and transport, office and everyday objects, weather. | 62 |

## How to type them

Every glyph sits on a keyboard key (shown below), and where a matching Unicode symbol exists it is *also* mapped there, so text like `┌──┐`, `★`, `✈` renders correctly too. Glyphs without a standard code point live in the Private Use Area.

**GUI:** box drawing is laid out as a 3×3 grid on the keyboard — `q w e / a s d / z x c` is single line `┌┬┐ / ├┼┤ / └┴┘`, `r` = `─`, `f` = `│`. Shift gives the double-line set. `t y u / g h j / b n m` (and shifted) are the mixed single/double sets, `i o / k l` are rounded corners.

**Shapes:** heavy arrows follow the numeric keypad (`8` up, `2` down, `4` left, `6` right, `7 9 1 3` diagonals).

## Files

- `fonts/<family>/*.otf` – desktop (CFF outlines)
- `fonts/<family>/*.ttf` – desktop / apps (TrueType outlines)
- `fonts/<family>/*.woff2` – web
- `svg/<family>/*.svg` – every glyph as a standalone SVG
- `specimens/*.png` – glyph charts
- `specimen.html` – interactive specimen + type tester (open in a browser)
- `source/` – the Python that draws and compiles everything (`python3 package.py`, needs `fonttools skia-pathops brotli pillow`)

## Web use

```css
@font-face { font-family: 'DingThats Objects'; src: url('DingThatsObjects-Regular.woff2') format('woff2'); }
.icon { font-family: 'DingThats Objects'; }
```

```html
<span class="icon">h</span> Home  <span class="icon">e</span> Contact
```

For accessibility, add `aria-hidden="true"` to decorative icons and give meaningful ones an `aria-label`.

## License

Copyright 2026 The DingThats Project Authors (https://dingthat.com). Licensed under the SIL Open Font License 1.1 — see `OFL.txt`. Free to use, embed, modify and redistribute; the fonts may not be sold on their own.

## DingThats GUI — character map

| Key | Glyph | Also mapped to |
|---|---|---|
| `q` | corner tl | U+250C Box Drawings Light Down And Right |
| `w` | tee down | U+252C Box Drawings Light Down And Horizontal |
| `e` | corner tr | U+2510 Box Drawings Light Down And Left |
| `a` | tee right | U+251C Box Drawings Light Vertical And Right |
| `s` | cross | U+253C Box Drawings Light Vertical And Horizontal |
| `d` | tee left | U+2524 Box Drawings Light Vertical And Left |
| `z` | corner bl | U+2514 Box Drawings Light Up And Right |
| `x` | tee up | U+2534 Box Drawings Light Up And Horizontal |
| `c` | corner br | U+2518 Box Drawings Light Up And Left |
| `r` | horizontal | U+2500 Box Drawings Light Horizontal |
| `f` | vertical | U+2502 Box Drawings Light Vertical |
| `Q` | dbl tl | U+2554 Box Drawings Double Down And Right |
| `W` | dbl tee dn | U+2566 Box Drawings Double Down And Horizontal |
| `E` | dbl tr | U+2557 Box Drawings Double Down And Left |
| `A` | dbl tee rt | U+2560 Box Drawings Double Vertical And Right |
| `S` | dbl cross | U+256C Box Drawings Double Vertical And Horizontal |
| `D` | dbl tee lt | U+2563 Box Drawings Double Vertical And Left |
| `Z` | dbl bl | U+255A Box Drawings Double Up And Right |
| `X` | dbl tee up | U+2569 Box Drawings Double Up And Horizontal |
| `C` | dbl br | U+255D Box Drawings Double Up And Left |
| `R` | dbl horiz | U+2550 Box Drawings Double Horizontal |
| `F` | dbl vert | U+2551 Box Drawings Double Vertical |
| `t` | mix tl | U+2552 Box Drawings Down Single And Right Double |
| `y` | mix tee dn | U+2564 Box Drawings Down Single And Horizontal Double |
| `u` | mix tr | U+2555 Box Drawings Down Single And Left Double |
| `g` | mix tee rt | U+255E Box Drawings Vertical Single And Right Double |
| `h` | mix cross | U+256A Box Drawings Vertical Single And Horizontal Double |
| `j` | mix tee lt | U+2561 Box Drawings Vertical Single And Left Double |
| `b` | mix bl | U+2558 Box Drawings Up Single And Right Double |
| `n` | mix tee up | U+2567 Box Drawings Up Single And Horizontal Double |
| `m` | mix br | U+255B Box Drawings Up Single And Left Double |
| `T` | mix2 tl | U+2553 Box Drawings Down Double And Right Single |
| `Y` | mix2 tee dn | U+2565 Box Drawings Down Double And Horizontal Single |
| `U` | mix2 tr | U+2556 Box Drawings Down Double And Left Single |
| `G` | mix2 tee rt | U+255F Box Drawings Vertical Double And Right Single |
| `H` | mix2 cross | U+256B Box Drawings Vertical Double And Horizontal Single |
| `J` | mix2 tee lt | U+2562 Box Drawings Vertical Double And Left Single |
| `B` | mix2 bl | U+2559 Box Drawings Up Double And Right Single |
| `N` | mix2 tee up | U+2568 Box Drawings Up Double And Horizontal Single |
| `M` | mix2 br | U+255C Box Drawings Up Double And Left Single |
| `i` | round tl | U+256D Box Drawings Light Arc Down And Right |
| `o` | round tr | U+256E Box Drawings Light Arc Down And Left |
| `k` | round bl | U+2570 Box Drawings Light Arc Up And Right |
| `l` | round br | U+256F Box Drawings Light Arc Up And Left |
| `1` | shade light | U+2591 Light Shade |
| `2` | shade medium | U+2592 Medium Shade |
| `3` | shade dark | U+2593 Dark Shade |
| `4` | full block | U+2588 Full Block |
| `5` | upper half | U+2580 Upper Half Block |
| `6` | lower half | U+2584 Lower Half Block |
| `7` | left half | U+258C Left Half Block |
| `8` | right half | U+2590 Right Half Block |
| `9` | square | U+25A0 Black Square |
| `0` | square white | U+25A1 White Square |
| `?` | small square | U+25AA Black Small Square |
| — | black rect | U+25AC Black Rectangle |
| `!` | smiley | U+263A White Smiling Face |
| `@` | smiley inv | U+263B Black Smiling Face |
| `#` | heart | U+2665 Black Heart Suit |
| `$` | diamond | U+2666 Black Diamond Suit |
| `%` | club | U+2663 Black Club Suit |
| `^` | spade | U+2660 Black Spade Suit |
| `&` | bullet | U+2022 Bullet |
| `*` | bullet inv | U+25D8 Inverse Bullet |
| `(` | circle | U+25CB White Circle |
| `)` | circle inv | U+25D9 Inverse White Circle |
| `-` | tri up | U+25B2 Black Up-Pointing Triangle |
| `=` | tri down | U+25BC Black Down-Pointing Triangle |
| `[` | pointer left | U+25C4 Black Left-Pointing Pointer |
| `]` | pointer right | U+25BA Black Right-Pointing Pointer |
| — | arrow up | U+2191 Upwards Arrow |
| — | arrow down | U+2193 Downwards Arrow |
| — | arrow left | U+2190 Leftwards Arrow |
| — | arrow right | U+2192 Rightwards Arrow |
| — | arrow up-down | U+2195 Up Down Arrow |
| — | arrow left-right | U+2194 Left Right Arrow |
| — | up-down base | U+21A8 Up Down Arrow With Base |
| — | right angle | U+221F Right Angle |
| — | note | U+266A Eighth Note |
| — | notes | U+266B Beamed Eighth Notes |
| — | sun | U+263C White Sun With Rays |
| — | house | U+2302 House |
| — | male | U+2642 Male Sign |
| — | female | U+2640 Female Sign |
| — | double excl | U+203C Double Exclamation Mark |
| — | pilcrow | U+00B6 Pilcrow Sign |
| `p` | checkbox | U+E000 Private Use |
| `P` | checkbox on | U+E001 Private Use, U+2611 Ballot Box With Check |
| `~` | checkbox mixed | U+E002 Private Use |
| `v` | radio | U+E003 Private Use |
| `V` | radio on | U+E004 Private Use |
| `I` | toggle off | U+E005 Private Use |
| `O` | toggle on | U+E006 Private Use |
| `_` | progress empty | U+E007 Private Use |
| `+` | progress full | U+E008 Private Use |
| `K` | progress L cap | U+E009 Private Use |
| `L` | progress R cap | U+E00A Private Use |
| `;` | close | U+E00B Private Use |
| `:` | maximize | U+E00C Private Use |
| `'` | minimize | U+E00D Private Use |
| `"` | restore | U+E00E Private Use |
| `,` | pointer | U+E00F Private Use |
| `.` | text cursor | U+E010 Private Use |
| `/` | hourglass | U+E011 Private Use, U+231B Hourglass |
| `<` | scroll left | U+E012 Private Use |
| `>` | scroll right | U+E013 Private Use |
| `{` | scroll up | U+E014 Private Use |
| `}` | scroll down | U+E015 Private Use |
| `\` | menu | U+E016 Private Use |
| `\|` | dropdown | U+E017 Private Use |
| `` ` `` | resize grip | U+E018 Private Use |

## DingThats Shapes — character map

| Key | Glyph | Also mapped to |
|---|---|---|
| `a` | triangle up | U+25B2 Black Up-Pointing Triangle |
| `b` | bullet | U+2022 Bullet |
| `c` | circle | U+25CF Black Circle |
| `d` | diamond | U+25C6 Black Diamond |
| `e` | ellipse | U+2B2C Black Horizontal Ellipse |
| `f` | burst | U+2738 Heavy Eight Pointed Rectilinear Black Star |
| `g` | cog | U+2699 Gear |
| `h` | heart | U+2665 Black Heart Suit |
| `i` | info | U+24D8 Circled Latin Small Letter I |
| `j` | corner | U+25E2 Black Lower Right Triangle |
| `k` | star | U+2605 Black Star |
| `l` | triangle left | U+25C0 Black Left-Pointing Triangle |
| `m` | menu | U+2630 Trigram For Heaven |
| `n` | octagon | U+2BC3 Horizontal Black Octagon |
| `o` | ring | U+25CB White Circle |
| `p` | pentagon | U+2B1F Black Pentagon |
| `q` | question | U+E100 Private Use |
| `r` | triangle right | U+25B6 Black Right-Pointing Triangle |
| `s` | square | U+25A0 Black Square |
| `t` | hexagon | U+2B22 Black Hexagon |
| `u` | power | U+23FB Power Symbol |
| `v` | check | U+2713 Check Mark |
| `w` | triangle down | U+25BC Black Down-Pointing Triangle |
| `x` | cross | U+2715 Multiplication X |
| `y` | sparkle | U+2726 Black Four Pointed Star |
| `z` | bolt | U+26A1 High Voltage Sign |
| `A` | warning | U+26A0 Warning Sign |
| `B` | square in sq | U+25A3 White Square Containing Black Small Square |
| `C` | fisheye | U+25C9 Fisheye |
| `D` | diamond white | U+25C7 White Diamond |
| `E` | circle minus | U+2296 Circled Minus |
| `F` | circle plus | U+2295 Circled Plus |
| `G` | circle cross | U+2297 Circled Times |
| `H` | heart white | U+2661 White Heart Suit |
| `I` | half left | U+25D0 Circle With Left Half Black |
| `J` | corner | U+25E3 Black Lower Left Triangle |
| `K` | star white | U+2606 White Star |
| `L` | tri left white | U+25C1 White Left-Pointing Triangle |
| `M` | ellipsis | U+22EF Midline Horizontal Ellipsis |
| `N` | prohibited | U+1F6C7 Prohibited Sign |
| `O` | bullseye | U+25CE Bullseye |
| `P` | play circle | U+E101 Private Use |
| `Q` | ballot box | U+2610 Ballot Box |
| `R` | tri right white | U+25B7 White Right-Pointing Triangle |
| `S` | square white | U+25A1 White Square |
| `T` | hexagon white | U+2B21 White Hexagon |
| `U` | eject | U+23CF Eject Symbol |
| `V` | ballot check | U+2611 Ballot Box With Check |
| `W` | tri down white | U+25BD White Down-Pointing Triangle |
| `X` | ballot x | U+2612 Ballot Box With X |
| `Y` | sparkle white | U+2727 White Four Pointed Star |
| `Z` | half right | U+25D1 Circle With Right Half Black |
| `8` | arrow up | U+2B06 Upwards Black Arrow |
| `2` | arrow down | U+2B07 Downwards Black Arrow |
| `4` | arrow left | U+2B05 Leftwards Black Arrow |
| `6` | arrow right | U+27A1 Black Rightwards Arrow |
| `7` | arrow up-left | U+2B09 North West Black Arrow |
| `9` | arrow up-right | U+2B08 North East Black Arrow |
| `1` | arrow down-left | U+2B0B South West Black Arrow |
| `3` | arrow down-right | U+2B0A South East Black Arrow |
| `5` | arrow up-down | U+2B0D Up Down Black Arrow |
| `0` | arrow left-right | U+2B0C Left Right Black Arrow |
| `!` | undo | U+21BA Anticlockwise Open Circle Arrow |
| `@` | chevron down | U+2304 Down Arrowhead |
| `#` | redo | U+21BB Clockwise Open Circle Arrow |
| `$` | chevron left | U+2039 Single Left-Pointing Angle Quotation Mark |
| `%` | refresh | U+27F3 Clockwise Gapped Circle Arrow |
| `^` | chevron right | U+203A Single Right-Pointing Angle Quotation Mark |
| `&` | expand diag | U+2922 North East And South West Arrow |
| `*` | chevron up | U+2303 Up Arrowhead |
| `(` | diag alt | U+2921 North West And South East Arrow |
| `)` | swap | U+21C4 Rightwards Arrow Over Leftwards Arrow |
| `+` | plus | U+2795 Heavy Plus Sign |
| `-` | minus | U+2796 Heavy Minus Sign |
| `=` | equals | U+E102 Private Use |
| `/` | divide | U+2797 Heavy Division Sign |
| `\` | asterisk | U+2731 Heavy Asterisk |
| `[` | skip prev | U+23EE Black Left-Pointing Double Triangle With Vertical Bar |
| `]` | skip next | U+23ED Black Right-Pointing Double Triangle With Vertical Bar |
| `{` | rewind | U+23EA Black Left-Pointing Double Triangle |
| `}` | fast forward | U+23E9 Black Right-Pointing Double Triangle |
| `;` | pause | U+23F8 Double Vertical Bar |
| `:` | stop | U+23F9 Black Square For Stop |
| `'` | record | U+23FA Black Circle For Record |
| `"` | play/pause | U+23EF Black Right-Pointing Triangle With Double Vertical Bar |
| `,` | small left | U+25C2 Black Left-Pointing Small Triangle |
| `.` | small right | U+25B8 Black Right-Pointing Small Triangle |
| `<` | dbl chev left | U+E103 Private Use |
| `>` | dbl chev right | U+E104 Private Use |
| `?` | exclaim circle | U+E105 Private Use |
| `\|` | ellipsis vert | U+22EE Vertical Ellipsis |
| `` ` `` | search | U+2315 Telephone Recorder |
| `~` | backspace | U+232B Erase To The Left |
| `_` | return | U+23CE Return Symbol |

## DingThats Objects — character map

| Key | Glyph | Also mapped to |
|---|---|---|
| `a` | airplane | U+2708 Airplane |
| `b` | bus | U+1F68C Bus |
| `c` | car | U+1F697 Automobile |
| `d` | document | U+1F4C4 Page Facing Up |
| `e` | envelope | U+2709 Envelope |
| `f` | factory | U+1F3ED Factory |
| `g` | fuel pump | U+26FD Fuel Pump |
| `h` | house | U+1F3E0 House Building |
| `i` | lightbulb | U+1F4A1 Electric Light Bulb |
| `j` | anchor | U+2693 Anchor |
| `k` | key | U+1F511 Key |
| `l` | lock | U+1F512 Lock |
| `m` | map pin | U+1F4CD Round Pushpin |
| `n` | bell | U+1F514 Bell |
| `o` | office | U+1F3E2 Office Building |
| `p` | person | U+1F464 Bust In Silhouette |
| `q` | people | U+1F465 Busts In Silhouette |
| `r` | rocket | U+1F680 Rocket |
| `s` | shop | U+1F3EA Convenience Store |
| `t` | train | U+1F686 Train |
| `u` | umbrella | U+2602 Umbrella |
| `v` | truck | U+1F69A Delivery Truck |
| `w` | globe | U+1F310 Globe With Meridians |
| `x` | taxi | U+1F695 Taxi |
| `y` | bicycle | U+1F6B2 Bicycle |
| `z` | cart | U+1F6D2 Shopping Trolley |
| `A` | alarm clock | U+23F0 Alarm Clock |
| `B` | bank | U+1F3E6 Bank |
| `C` | calendar | U+1F4C5 Calendar |
| `D` | desktop | U+1F5A5 Desktop Computer |
| `E` | school | U+1F3EB School |
| `F` | folder | U+1F4C1 File Folder |
| `G` | gift | U+1F381 Wrapped Present |
| `H` | hospital | U+1F3E5 Hospital |
| `I` | camera | U+1F4F7 Camera |
| `J` | briefcase | U+1F4BC Briefcase |
| `K` | keyboard | U+2328 Keyboard |
| `L` | laptop | U+1F4BB Personal Computer |
| `M` | mobile | U+1F4F1 Mobile Phone |
| `N` | cloud | U+2601 Cloud |
| `O` | clock | U+1F552 Clock Face Three Oclock |
| `P` | printer | U+1F5A8 Printer |
| `Q` | shopping bag | U+1F6CD Shopping Bags |
| `R` | restaurant | U+1F374 Fork And Knife |
| `S` | sun | U+2600 Black Sun With Rays |
| `T` | traffic light | U+1F6A6 Vertical Traffic Light |
| `U` | trash | U+1F5D1 Wastebasket |
| `V` | tent | U+26FA Tent |
| `W` | partly cloudy | U+26C5 Sun Behind Cloud |
| `X` | telephone | U+260E Black Telephone |
| `Y` | sailboat | U+26F5 Sailboat |
| `Z` | moon | U+1F319 Crescent Moon |
| `1` | tree | U+1F333 Deciduous Tree |
| `2` | castle | U+1F3F0 European Castle |
| `3` | ship | U+1F6A2 Ship |
| `4` | tram | U+1F68B Tram Car |
| `5` | bridge | U+1F309 Bridge At Night |
| `6` | battery | U+1F50B Battery |
| `7` | parking | U+1F17F Negative Squared Latin Capital Letter P |
| `8` | bus stop | U+1F68F Bus Stop |
| `9` | wrench | U+1F527 Wrench |
| `0` | flag | U+2691 Black Flag |
