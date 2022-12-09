Link to labs : https://systems-rg.github.io/wss22-cloud-labs.html

Relevant part for day 1 labs :
![image](https://user-images.githubusercontent.com/55680959/206789956-b3264f48-c260-4a29-84f2-03cd97b4e615.png)

---

Misc Notes :

- Python serial program for word count
- Python parallel program using processes for word count
- Plots to compare time taken in both cases

Note : should observe speedup in parallel case

output for word count serial program
```
(wss2-env) (base) kushalj@kushalj-Precision-5550:~/Documents/iitd-wss22/day1$ time python wc-single-process.py 
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m3.545s
user    0m3.405s
sys     0m0.140s
```


output for word count parallel program

we keep files same and change number of processes :

2
```
(wss2-env) (base) kushalj@kushalj-Precision-5550:~/Documents/iitd-wss22/day1$ time python wc-multi-process.py
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m2.294s
user    0m4.400s
sys     0m0.363s
```

4
```
(wss2-env) (base) kushalj@kushalj-Precision-5550:~/Documents/iitd-wss22/day1$ time python wc-multi-process.py 
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m1.655s
user    0m4.785s
sys     0m0.360s
```

6
```
(wss2-env) (base) kushalj@kushalj-Precision-5550:~/Documents/iitd-wss22/day1$ time python wc-multi-process.py 
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m1.459s
user    0m4.930s
sys     0m0.452s
```

8
```
(wss2-env) (base) kushalj@kushalj-Precision-5550:~/Documents/iitd-wss22/day1$ time python wc-multi-process.py 
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m1.377s
user    0m5.277s
sys     0m0.428s
```

10
```
(wss2-env) (base) kushalj@kushalj-Precision-5550:~/Documents/iitd-wss22/day1$ time python wc-multi-process.py 
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m1.386s
user    0m5.253s
sys     0m0.466s
```

12
```
(wss2-env) (base) kushalj@kushalj-Precision-5550:~/Documents/iitd-wss22/day1$ time python wc-multi-process.py 
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m1.409s
user    0m5.368s
sys     0m0.554s
```

20
```
(wss2-env) (base) kushalj@kushalj-Precision-5550:~/Documents/iitd-wss22/day1$ time python wc-multi-process.py 
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m1.311s
user    0m6.086s
sys     0m0.558s
```

40
```
(wss2-env) (base) kushalj@kushalj-Precision-5550:~/Documents/iitd-wss22/day1$ time python wc-multi-process.py 
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m1.398s
user    0m6.733s
sys     0m0.715s
```

100
```
(wss2-env) (base) kushalj@kushalj-Precision-5550:~/Documents/iitd-wss22/day1$ time python wc-multi-process.py 
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m1.482s
user    0m6.731s
sys     0m0.682s
```

obs : runtime kinda saturates after 10 processes and does not improve further


Now, we keep num workers same and increase the number of files

NUM WORKERS = 4

files = 10
```
the 104181
and 70484
of 66795
to 64590
I 53640
a 51764
in 40583
that 30152
my 27103
you 25690

real    0m0.573s
user    0m1.082s
sys     0m0.145s
```

20
```
the 167963
and 111219
of 109396
to 105779
a 79646
I 66317
in 62930
that 46398
his 43592
with 39373

real    0m0.669s
user    0m1.547s
sys     0m0.167s
```
30
```
the 251566
and 168426
of 165239
to 160241
a 120592
I 99788
in 94713
that 69592
his 66427
with 59919

real    0m0.895s
user    0m2.291s
sys     0m0.180s
```
40
```
the 355041
and 235277
of 228445
to 218920
a 168487
I 138737
in 132336
that 96305
his 89601
with 81848

real    0m1.062s
user    0m2.989s
sys     0m0.237s
```
50
```
the 446976
and 298772
of 281366
to 273192
a 212893
I 175919
in 165096
that 120778
his 108755
with 101503

real    0m1.309s
user    0m3.928s
sys     0m0.326s
```
60
```
the 530184
and 355608
of 333108
to 325338
a 252900
I 209934
in 195900
that 143712
his 128634
with 120468

real    0m1.565s
user    0m4.669s
sys     0m0.360s
```
