#lang racket
; 练习 1.9
(define (inc x) (+ x 1))
(define (dec x) (- x 1))

(define (plus-1 a b) ; 线性递归
 (if (= a 0)
     b
     (inc (plus-1 (dec a) b))))

(define (plus-2 a b) ; 线性迭代
 (if (= a 0)
     b
     (plus-2 (dec a) (inc b))))

; test
(plus-1 3 4)
(plus-2 3 4)