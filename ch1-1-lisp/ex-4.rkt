#lang racket
; 练习 1.4
(define (a-plus-abs-b a b) ((if (> b 0) + -) a b))

; test
(a-plus-abs-b 3 4)
(a-plus-abs-b 3 -4)