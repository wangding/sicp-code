#lang racket
; 1.2.1 线性的递归和迭代
; 求阶乘
(define (factorial-a n)
 (if (= n 1)
 1
 (* n (factorial-a (- n 1)))))

; test
(factorial-a 6)

(define (factorial-b n)
 (define (fact-iter product counter)
  (if (> counter n)
      product
      (fact-iter (* counter product)
                 (+ counter 1))))
  (fact-iter 1 1))

; test
(factorial-b 6)
