class ElectricFieldStream(Scene):
    def construct(self):

        Charges = np.array([
            [1, -2, 0],
            [-1, 2, 0]
        ])


        def E_field(pos):
            x, y = pos[0], pos[1]
            Ex, Ey = 0, 0
            for q, x0, y0 in Charges:
                dx = x - x0
                dy = y - y0
                r2 = dx**2 + dy**2
                if r2 < 1e-4:
                    continue
                r = np.sqrt(r2)
                Ex += q * dx / r**3
                Ey += q * dy / r**3

            magn = np.sqrt(Ex**2 + Ey**2) + 1e-8
            if magn > 2:
                Ex *= 2 / magn
                Ey *= 2 / magn

            return Ex * RIGHT + Ey * UP


        stream_lines = StreamLines(
            E_field,
            stroke_width=3,
            max_anchors_per_line=30,
            virtual_time=7,
            x_range=[-8, 8, 0.4],
            y_range=[-7, 7, 0.4])

        self.add(stream_lines)
        vf = ArrowVectorField(E_field, x_range=[-8, 8, 0.3], y_range=[-7, 7, 0.3])
        self.add(vf)

        stream_lines.start_animation(flow_speed=1.5, warm_up=False)


        #axes = NumberPlane(x_range=[-8, 8], y_range=[-6, 6])
        #self.add(axes)

        charge_dots = VGroup()
        for q, x0, y0 in Charges:
            color = RED if q > 0 else BLUE
            dot = Dot(point=np.array([x0, y0, 0]), color=color, radius=0.2)
            charge_dots.add(dot)
        self.add(charge_dots)

        self.wait(stream_lines.virtual_time / 1.5)
