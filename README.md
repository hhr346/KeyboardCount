# README

操作步骤：

1. 直接运行 `Keyboard.py` 文件，当终端出现：`Start Tapping now` 时，就可以对之后键入的所有按键进行记录。
2. 当想结束记录时，按下F11退出（如果开启了`Fnlock`则需要按下`Fn+F11`），或者可以考虑自定义组合键来推出当前的记录；
3. 自动产生一张和键盘对应的图；

> 注意事项：不能睡眠！否则退出不了！但是若是休眠短时间还可以进行退出



Steps:

1. `py Keyboard.py` to run the script, when the terminal shows `Start Tapping now`, the program will keep track on whatever you tap now;
2. When you want to stop the tracking, just tap `F11` to stop(`Fn+F11` if you turn on the `Fnlock`);
3. Generate a heatmap graph to show your tapping frequency corresponding to each key;

> Caution: During the tracking process, you can't let the computer to enter sleep mode, or it can't be stopped by `F11` 



![example](.\example.png)

Here is an example graph of the output, and it can actually reveal a lot of things, as you can see:

1. I'm a fan of Vim because `J` and `K` is tapped a lot. 
2. Interestingly,  `Q` and `Z` are rarely tapped.
3. No one use the RIGHT `ctrl` and `shift` and `alt` 



Also, it still has a lot to improve: 

1. the layout is ugly, and not very like a keyboard;
2. the character on the key can be shown on the keyboard, too;
3. the program counts the key tap number by the tap value, so it goes wrong when two values share the same key, like `:` `;` 

