#lang racket
; 1.3.2 用 lambda 构造过程

; (lambda (x) (+ x 4))
; (lambda (x) (/ 1.0 (* x (+ x 2))))

(define (sum term a next b)
  (if (> a b)
    0
    (+ (term a)
       (sum term (next a) next b))))

; pi-sum 函数不需要定义两个很少用到的函数 pi-term, pi-next
; lambda 匿名函数搞定
(define (pi-sum a b)
  (sum (lambda (x) (/ 1.0 (* x (+ x 2))))
       a
       (lambda (x) (+ x 4))
       b))

; test
(pi-sum 1 7) ; 0.3619047619047619

; integral 函数不需要定义函数 add-dx, 用 lambda 匿名函数代替
(define (integral f a b dx)
  (* (sum f
         (+ a (/ dx 2.0))
         (lambda (x) (+ x dx))
         b)
     dx))

; test
(define (cube x) (* x x x))
(integral cube 0 1 0.01)  ; .24998750000000042

(define (plus4 x) (+ x 4))
(define plus4 (lambda (x) (+ x 4)))
(define (square x) (* x x))

; 等价于 javascipt 中的函数立即执行表达式
; Immediately Invoked Function Expression, IIFE
((lambda (x y z) (+ x y (square z)))
 1 2 3)

(define (f x y)
  (define (f-helper a b)
    (+ (* x (square a))
       (* y b)
       (* a b)))
  (f-helper (+ 1 (* x y)) (- 1 y)))

(define (f x y)
  ((lambda (a b)
      (+ (* x (square a))
         (* y b)
         (* a b)))
   (+ 1 (* x y))
   (- 1 y)))

(define (f x y)
  (let ((a (+ 1 (* x y)))
        (b (- 1 y)))
  (+ (* x (square a))
     (* y b)
     (* a b))))