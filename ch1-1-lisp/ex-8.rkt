#lang racket
; 练习 1.8
(define (cbrt x)
 (define (improve guess) 
   (/ (+ (/ x (* guess guess)) (* 2 guess)) 3))
 (define (good-enough? guess)
   (let ((next-guess (improve guess)))
   (< (abs (- next-guess guess)) (* guess 0.001))))
 (define (cbrt-iter guess)
   (if (good-enough? guess)
       guess
       (cbrt-iter (improve guess))))
 (cbrt-iter 1.0))

; test
(cbrt 9) ; 2.0801035255095734
(cbrt 0.25) ; 0.6304661123708742
(cbrt 0.0001) ; 0.046419202576589325
(cbrt 10000886699) ; 2154.5043672873685
(cbrt 8) ; 2.000004911675504