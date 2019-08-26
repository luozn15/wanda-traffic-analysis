(defun c:DPLK()
  (setvar "cmdecho" 0)
  (setq fileph (getfiled "选择文件存储路径" "" "csv" 1));选择文件存储路径
  (princ "\n请选择店铺标号(名称):")
  (setq ss (entsel))
  (setq ptlist "")
  (while ss
    (setq ss (car ss))
    (setq ss_data (entget ss))
    (setq wb (cdr (assoc 1 ss_data)));提取店铺编号/名称
    (princ "\n请选择该店铺轮廓线:");提取店铺轮廓线
    (setq el (car (entsel)))
    (foreach n (entget el)
      (if (= 10 (car n))
      (setq ptlist (cons (cdr n) ptlist)))
     )
    (setq aa (list wb ":" ptlist))
    ;改变已选择轮廓的颜色
    (entmod(append(entget el)'((62 . 2))))
    ;改变已选择轮廓线的粗细
    (entmod(append(entget el)'((370 . 50))))
    ;确认勾选完成输出数据或重新勾选不输出数据
    (princ "\n继续勾选<Enter>重新勾选<Z>")
    (setq j (getstring))
    (if (= j "")
      (writedata))
    (if (= j "z")
      (setq el_data (subst k (assoc 62 el_data) el_data)))
    (if (= j "z")
      (setq el_data (subst h (assoc 360 el_data) el_data)))
    (entmod el_data)
    (setq ptlist "")
    (princ "\n请选择店铺标号(名称):")
    (setq ss (entsel))
    )
  (princ)
 )


(defun writedata()
  (setq file (open fileph "a"))
  (princ aa file)
  (princ "\n" file)
  (close file)
  )
