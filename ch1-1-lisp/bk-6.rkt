#lang racket
; 1.1.6 条件表达式和谓词
(define (abs1 x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))))

; test
(abs1 1)
(abs1 -1)
(abs1 0)

(define (abs2 x)
 (cond ((< x 0) (- x))
       (else x)))

; test
(abs2 2)
(abs2 -2)
(abs2 0)

; -- if 是 cond 的语法糖
(define (abs3 x)
 (if (< x 0)
     (- x)
     x))

; test
(abs3 3)
(abs3 -3)
(abs3 0)

; and, or, not 逻辑运算
(define x 8)  ; try x=18 
(and (> x 5) (< x 10))

;(define (>= x y) (or (> x y) (= x y)))
(define (>= x y) (not (< x y)))

; test
>=
(>= 5 6)
