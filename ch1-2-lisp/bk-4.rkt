#lang racket
; 1.2.4 求幂
; 线性递归
(define (expt1 b n)
 (if (= n 0)
     1
     (* b (expt1 b (- n 1)))))

; 线性迭代
(define (expt2 b n)
  (define (expt-iter b counter product)
     (if (= counter 0)
         product
         (expt-iter b (- counter 1) (* b product))))
  (expt-iter b n 1))

; 快速递归
(define (expt3 b n)
  (define (square x) (* x x))
  (cond ((= n 0) 1)
        ((even? n) (square (expt3 b (/ n 2))))
        (else (* b (expt3 b (- n 1))))))

; test
(expt1 2 3)
(expt2 2 3)
(expt3 2 3)