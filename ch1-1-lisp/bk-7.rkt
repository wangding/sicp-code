#lang racket
; 1.1.7 实例：牛顿法求平方根
(define (square x) (* x x))
(define (average x y) (/ (+ x y) 2))
(define (improve guess x)
 (average guess (/ x guess)))
(define (good-enough? guess x)
 (< (abs (- (square guess) x)) 0.001))
(define (sqrt-iter guess x)
 (if (good-enough? guess x)
     guess
     (sqrt-iter (improve guess x) x)))
(define (sqrt x) (sqrt-iter 1.0 x))

; test
(sqrt 9) ; 3.00009155413138
(sqrt (+ 100 37)) ; 11.704699917758145
(sqrt (+ (sqrt 2) (sqrt 3))) ; 1.7739279023207892
(square (sqrt 1000)) ; 1000.000369924366
(sqrt 0.25) ; 0.5001524390243902