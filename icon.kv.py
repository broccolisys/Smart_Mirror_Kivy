  Button:
        text: ""
        on_press: gif.anim_delay = 0.10
        on_press: gif._coreimage.anim_reset(True)
        Image:
            id: gif
            source:'./icons/webview5.zip'
            center: self.parent.center
            size: 500, 500
            allow_stretch: True
            anim_delay: 0
            anim_loop: 1
            keep_ratio: False
            keep_data: True



