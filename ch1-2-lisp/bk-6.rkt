#lang racket
; 1.2.6 素数检查

; 蛮力法

; 检查 n 是否为素数
(define (square x) (* x x))
(define (prime1? n)
  ; 找 n 的因子
  (define (find-divisor test-divisor)
    (define (divides? a b) (= (remainder b a) 0))
    (cond ((> (square test-divisor) n) n)
          ((divides? test-divisor n) test-divisor)
          (else (find-divisor (+ test-divisor 1)))))  
  (= n (find-divisor 2)))

; test
(prime1? 7)
(prime1? 8)

; 费马检查
(define (expmod base exp m)
   (cond ((= exp 0) 1)
         ((even? exp) (remainder (square (expmod base (/ exp 2) m)) m))
         (else (remainder (* base (expmod base (- exp 1) m)) m))))

(define (fermat-test n)
 (define (try-it a) (= (expmod a n n) a))
 (try-it (+ 1 (random (- n 1)))))

(define (prime2? n times)
 (cond ((= times 0) true)
       ((fermat-test n) (prime2? n (- times 1)))
       (else false)))

; test
(prime2? 7 1)
(prime2? 8 1)
(prime2? 7 3)
(prime2? 8 3)