BEGIN{r200=0; r301=0; r304=0; r404=0;}
$9==200{r200++; next;}
$9==301{r301++; next;}
$9==304{r304++; next;}
$9==404{r404++; next;}
END{print "OK: " r200;
    print "Moved Permanently: " r301;
    print "Not Modified: " r304;
    print "Not Found: " r404;
    print "Others: " NR-r200-r301-r304-r404;
    print "Total: " NR}
