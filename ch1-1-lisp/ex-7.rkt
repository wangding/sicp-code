#lang racket
; 练习 1.7
(define (sqrt x)
 (define (square x) (* x x))
 (define (average x y) (/ (+ x y) 2))
 (define (good-enough? guess)
   (let ((next-guess (improve guess)))
   (< (abs (- next-guess guess)) (* guess 0.001))))
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

; 很小的数和很大的数表现都非常好
(sqrt 0.0001) ; 0.010000714038711746
(sqrt 10000886699) ; 100010.02267281363