# FancyText
𝗧𝘂𝗿𝗻 𝘆𝗼𝘂𝗿 𝗮𝘀𝗰𝗶𝗶 𝘁𝗲𝘅𝘁 𝗶𝗻𝘁𝗼 𝗮 𝗳𝗮𝗻𝗰𝘆 ⓕⓞⓝⓣ.

![FancyText Tests](https://api.travis-ci.org/freejoe76/fancytext.png)

## Credits
Translation matrix via [Moses Moore](https://github.com/mozai/). [View his web-facing character translator here](http://mozai.com/programming/dandytype.html).

## Usage
```
# Basic:
./fancytext.py HEY FANCY THIS IS MONOSPACED, RIGHT?
𝙷𝙴𝚈 𝙵𝙰𝙽𝙲𝚈 𝚃𝙷𝙸𝚂 𝙸𝚂 𝙼𝙾𝙽𝙾𝚂𝙿𝙰𝙲𝙴𝙳, 𝚁𝙸𝙶𝙷𝚃?

# Choose a font:
./fancytext.py --font circled now you have circles
ⓝⓞⓦ ⓨⓞⓤ ⓗⓐⓥⓔ ⓒⓘⓡⓒⓛⓔⓢ
```

## Testing
```
python3 -m pytest
```

## Building

https://setuptools.readthedocs.io/en/latest/setuptools.html#develop-deploy-the-project-source-in-development-mode

## Font options:

parens, circled, bold, italic, bolditalic, script, boldscript, fraktur, doublestruck, boldfraktur, sansserif, sserifbold, sserifitalic, sserifbold, sserifitalic, sserifboldi, monospace, fullwidth.
```
./fancytext.py --font parens HEY this is parens
⒣⒠⒴ ⒯⒣⒤⒮ ⒤⒮ ⒫⒜⒭⒠⒩⒮
./fancytext.py --font circled HEY this is circled
ⒽⒺⓎ ⓣⓗⓘⓢ ⓘⓢ ⓒⓘⓡⓒⓛⓔⓓ
./fancytext.py --font bold HEY this is bold
𝐇𝐄𝐘 𝐭𝐡𝐢𝐬 𝐢𝐬 𝐛𝐨𝐥𝐝
./fancytext.py --font italic HEY this is italic
𝐻𝐸𝑌 𝑡𝑕𝑖𝑠 𝑖𝑠 𝑖𝑡𝑎𝑙𝑖𝑐
./fancytext.py --font bolditalic HEY this is bolditalic
𝑯𝑬𝒀 𝒕𝒉𝒊𝒔 𝒊𝒔 𝒃𝒐𝒍𝒅𝒊𝒕𝒂𝒍𝒊𝒄
./fancytext.py --font script HEY this is script
𝒣𝒠𝒴 𝓉𝒽𝒾𝓈 𝒾𝓈 𝓈𝒸𝓇𝒾𝓅𝓉
./fancytext.py --font boldscript HEY this is boldscript
𝓗𝓔𝓨 𝓽𝓱𝓲𝓼 𝓲𝓼 𝓫𝓸𝓵𝓭𝓼𝓬𝓻𝓲𝓹𝓽
./fancytext.py --font fraktur HEY this is fraktur
𝔋𝔈𝔜 𝔱𝔥𝔦𝔰 𝔦𝔰 𝔣𝔯𝔞𝔨𝔱𝔲𝔯
./fancytext.py --font doublestruck HEY this is doublestruck
𝔿𝔼𝕐 𝕥𝕙𝕚𝕤 𝕚𝕤 𝕕𝕠𝕦𝕓𝕝𝕖𝕤𝕥𝕣𝕦𝕔𝕜
./fancytext.py --font boldfraktur HEY this is boldfraktur
𝕳𝕰𝖄 𝖙𝖍𝖎𝖘 𝖎𝖘 𝖇𝖔𝖑𝖉𝖋𝖗𝖆𝖐𝖙𝖚𝖗
./fancytext.py --font sansserif HEY this is sansserif
𝖧𝖤𝖸 𝗍𝗁𝗂𝗌 𝗂𝗌 𝗌𝖺𝗇𝗌𝗌𝖾𝗋𝗂𝖿
./fancytext.py --font sserifbold HEY this is sserifbold
𝗛𝗘𝗬 𝘁𝗵𝗶𝘀 𝗶𝘀 𝘀𝘀𝗲𝗿𝗶𝗳𝗯𝗼𝗹𝗱
./fancytext.py --font sserifitalic HEY this is sserifitalic
𝘏𝘌𝘠 𝘵𝘩𝘪𝘴 𝘪𝘴 𝘴𝘴𝘦𝘳𝘪𝘧𝘪𝘵𝘢𝘭𝘪𝘤
./fancytext.py --font sserifbold HEY this is sserifbold
𝗛𝗘𝗬 𝘁𝗵𝗶𝘀 𝗶𝘀 𝘀𝘀𝗲𝗿𝗶𝗳𝗯𝗼𝗹𝗱
./fancytext.py --font sserifitalic HEY this is sserifitalic
𝘏𝘌𝘠 𝘵𝘩𝘪𝘴 𝘪𝘴 𝘴𝘴𝘦𝘳𝘪𝘧𝘪𝘵𝘢𝘭𝘪𝘤
./fancytext.py --font sserifboldi HEY this is sserifboldi
𝙃𝙀𝙔 𝙩𝙝𝙞𝙨 𝙞𝙨 𝙨𝙨𝙚𝙧𝙞𝙛𝙗𝙤𝙡𝙙𝙞
./fancytext.py --font monospace HEY this is monospace
𝙷𝙴𝚈 𝚝𝚑𝚒𝚜 𝚒𝚜 𝚖𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎
```

