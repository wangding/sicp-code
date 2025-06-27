#lang racket
; 习题 1.6
(define (new-if predicate then-clause else-clause)
 (cond (predicate then-clause)
       (else else-clause)))
(new-if (= 2 3) 0 5) ; 5
(new-if (= 1 1) 0 5) ; 0

(define (square x) (* x x))
(define (average x y) (/ (+ x y) 2))
(define (improve guess x) (average guess (/ x guess)))
(define (good-enough? guess x)
 (< (abs (- (square guess) x)) 0.001))
(define (sqrt-iter guess x)
 (new-if (good-enough? guess x)
         guess
         (sqrt-iter (improve guess x) x)))
(define (sqrt x)
 (sqrt-iter 1.0 x))

; test
(sqrt 9)
; 程序会死掉，因为应用序，new-if 直接对参数 sqrt-iter 求值
; 本来如果满足 good-enough? 应该不用执行 sqrt-iter
; 满足 good-enough? 应该是递归的退出条件，但是没有起到作用