#lang racket
; 1.1.8 过程作为黑盒抽象
(define (sqrt x)
 (define (square x) (* x x))
 (define (average x y) (/ (+ x y) 2))
 (define (good-enough? guess)
   (< (abs (- (square guess) x)) 0.001))
 (define (improve guess) (average guess (/ x guess)))
 (define (sqrt-iter guess)
   (if (good-enough? guess)
       guess
       (sqrt-iter (improve guess))))
 (sqrt-iter 1.0))

; test
(sqrt 9) ; 3.00009155413138
(sqrt (+ 100 37)) ; 11.704699917758145
(sqrt (+ (sqrt 2) (sqrt 3))) ; 1.7739279023207892
(sqrt 0.25) ; 0.5

; 大数和小数的精度问题
(sqrt 0.0001) ; 0.03230844833048122
(sqrt 10000886699) ; 100004.43339672497