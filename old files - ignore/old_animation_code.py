
## To insert into block 24 if required
## Doesn't exactly work as expected


anim = animation.FuncAnimation(fig, animate, init_func=init_func,
                              frames=clean_cb["YEAR"].unique().size, interval=1000)
anim.save('basic_animation.mp4', fps=1, extra_args=['-vcodec', 'libx264'])