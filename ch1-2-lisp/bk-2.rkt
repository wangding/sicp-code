#lang racket
; 1.2.2 树形递归
; 求斐波那契数列
(define (fib1 n) ; 树形递归
 (cond ((= n 0) 0)
       ((= n 1) 1)
       (else (+ (fib1 (- n 1)) (fib1 (- n 2))))))

(define (fib2 n) ; 线性迭代
  (define (fib-iter a b count)
   (if (= count 0)
       b
       (fib-iter (+ a b) a (- count 1))))
  (fib-iter 1 0 n))

; test
(fib1 6)
(fib2 6)

; 换零钱
; denomination 货币的面值
(define (count-change amount) 
 (define (first-denomination kinds-of-coins)
    (cond ((= kinds-of-coins 1) 1)
          ((= kinds-of-coins 2) 5)
          ((= kinds-of-coins 3) 10)
          ((= kinds-of-coins 4) 25)
          ((= kinds-of-coins 5) 50)))
  (define (cc amount kinds-of-coins)
    (cond ((= amount 0) 1)
          ((or (< amount 0) (= kinds-of-coins 0)) 0)
          (else (+ (cc amount (- kinds-of-coins 1))
                   (cc (- amount (first-denomination kinds-of-coins))
                       kinds-of-coins)))))
  (cc amount 5))

; test
(count-change 100)
