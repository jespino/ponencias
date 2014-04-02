function inttochar (value) {
     if (value==1) ret="a"
     if (value==2) ret="b"
     if (value==3) ret="c"
     if (value==4) ret="d"
     if (value==5) ret="e"
     if (value==6) ret="f"
     if (value==7) ret="g"
     if (value==8) ret="h"
     if (value==9) ret="i"
     if (value==10) ret="j"
     if (value==11) ret="k"
     if (value==12) ret="l"
     if (value==13) ret="m"
     if (value==14) ret="n"
     if (value==15) ret="ñ"
     if (value==16) ret="o"
     if (value==17) ret="p"
     if (value==18) ret="q"
     if (value==19) ret="r"
     if (value==20) ret="s"
     if (value==21) ret="t"
     if (value==22) ret="u"
     if (value==23) ret="v"
     if (value==24) ret="w"
     if (value==25) ret="x"
     if (value==26) ret="y"
     if (value==27) ret="z"
     return ret
}

BEGIN { for (x = 1; x <= 27; x++) {arr1[x]=0; arr2[x]=0; arr3[x]=0; }; mayorde27=0; totallongitud=0 }
/^a/{arr1[1]++};/^b/{arr1[2]++};/^c/{arr1[3]++};/^d/{arr1[4]++}
/^d/{arr1[5]++};/^e/{arr1[6]++};/^f/{arr1[7]++};/^g/{arr1[8]++}
/^h/{arr1[9]++};/^i/{arr1[10]++};/^j/{arr1[11]++};/^k/{arr1[12]++}
/^l/{arr1[13]++};/^m/{arr1[14]++};/^n/{arr1[15]++};/^ñ/{arr1[16]++}
/^o/{arr1[17]++};/^p/{arr1[18]++};/^q/{arr1[19]++};/^r/{arr1[20]++}
/^s/{arr1[21]++};/^t/{arr1[22]++};/^u/{arr1[23]++};/^w/{arr1[24]++}
/^x/{arr1[25]++};/^y/{arr1[26]++};/^z/{arr1[27]++};

/a$/{arr2[1]++};/b$/{arr2[2]++};/c$/{arr2[3]++};/d$/{arr2[4]++}
/d$/{arr2[5]++};/e$/{arr2[6]++};/f$/{arr2[7]++};/g$/{arr2[8]++}
/h$/{arr2[9]++};/i$/{arr2[10]++};/j$/{arr2[11]++};/k$/{arr2[12]++}
/l$/{arr2[13]++};/m$/{arr2[14]++};/n$/{arr2[15]++};/ñ$/{arr2[16]++}
/o$/{arr2[17]++};/p$/{arr2[18]++};/q$/{arr2[19]++};/r$/{arr2[20]++}
/s$/{arr2[21]++};/t$/{arr2[22]++};/u$/{arr2[23]++};/w$/{arr2[24]++}
/x$/{arr2[25]++};/y$/{arr2[26]++};/z$/{arr2[27]++};

{ l = length($0); if (l<=27) arr3[l]++; else mayorde27++; totallongitud=totallongitud+l;}
END {
	print "Palabras que empiezan por: "
	for (x = 1; x <= 27; x++) print inttochar(x)": "arr1[x]
	print "Palabras que terminen por: "
	for (x = 1; x <= 27; x++) print inttochar(x)": "arr2[x]
	print "Total de palabras: "NR

	print "Longitud de las palabras: "
	for (x= 1; x <= 27; x++) print x": "arr3[x]
	print ">27: "mayorde27

	print "Longitud media de las palabras: "(totallongitud/NR)
}

