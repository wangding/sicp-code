#lang racket
; 1.3.1 过程作为参数

; 问题 1：a~b 中 n 个连续的数求和，例如：1+2+3+...+100
(define (sum-integers a b)
  (if (> a b)
    0
    (+ a (sum-integers (+ a 1) b))))

; test
(sum-integers 1 100)

; 问题 2：a~b 中 n 个连续的数的立方求和，例如：1^3 + 2^3 +...+ 100^3
(define (cube x) (* x x x))
(define (sum-cubes a b)
  (if (> a b)
    0
    (+ (cube a) (sum-cubes(+ a 1) b))))

; test
(sum-cubes 1 3) ; 36

; 问题 3：计算 1/(1*3) + 1/(5*7) + ...
(define (pi-sum a b)
  (if (> a b)
    0
    (+ (/ 1.0 (* a (+ a 2)))
       (pi-sum (+ a 4) b))))

; test
(pi-sum 1 7) ; 0.3619047619047619

; 从上面三个求和的问题求解中抽取 sum 求和模式，这个是高阶函数
; 其中 term 是根据 a 计算数列中第 i 个数，例如：a^3
; 其中 next 是根据 a 计算下一个 a，例如：a + 1
(define (sum term a next b)
  (if (> a b)
    0
    (+ (term a)
       (sum term (next a) next b))))

; 用求和模式求解问题 1
(define (identity x) x)
(define (inc n) (+ n 1))
(define (sum-integers2 a b) (sum identity a inc b))

; test
(sum-integers2 1 100)

; 用求和模式求解问题 2
(define (sum-cubes2 a b) (sum cube a inc b))

; test
(sum-cubes2 1 3) ; 36

; 用求和模式求解问题 3
(define (pi-sum2 a b)
 (define (pi-term x) (/ 1.0 (* x (+ x 2))))
 (define (pi-next x) (+ x 4))
 (sum pi-term a pi-next b))

; test
(pi-sum2 1 7) ; 0.3619047619047619

; 用求和模式求解问题 4，求函数在 [a, b] 区间的定积分的近似值
(define (integral f a b dx)
 (define (add-dx x) (+ x dx))
 (* (sum f (+ a (/ dx 2.0)) add-dx b) dx))

(integral cube 0 1 0.01)  ; .24998750000000042
(integral cube 0 1 0.001) ; .249999875000001