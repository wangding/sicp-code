#lang racket
; 练习 1.5
(define (p) (p))
(define (test x y) (if (= x 0) 0 y))

; test
(test 0 (p))

; 程序出现死循环，所以是应用序，先求解 p，触发递归调用（死循环）
; 不是正则序