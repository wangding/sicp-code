#lang racket
; 1.1.4 复合过程（就是函数）
(define (square x) (* x x))
square
+

; test
(square 21)
(square (+ 2 5))
(square (square 3))

(define (sum-of-squares x y)
  (+ (square x) (square y)))

; test
(sum-of-squares 3 4)

(define (f a)
  (sum-of-squares (+ a 1) (* a 2)))
(f 5)