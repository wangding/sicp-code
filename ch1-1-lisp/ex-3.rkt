#lang racket
; 练习 1.3
(define (max-sum-square x y z)
  (define (square x) (* x x))
  ; (square 4)
  (define (sum-square x y) (+ (square x) (square y)))
  ; (sum-square 3 4)
  (cond ((and (< x y) (< x z)) (sum-square y z))
        ((and (< y x) (< y z)) (sum-square x z))
        ((and (< z x) (< z y)) (sum-square x y))
        )
  )

; test
(max-sum-square 3 4 5)