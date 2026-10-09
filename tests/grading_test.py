from matplotlib.testing.decorators import image_comparison
import matplotlib.pyplot as plt
import numpy as np
import zodiac

def test_plot_png():
    deco = image_comparison(baseline_images=['plot'], remove_text=False, extensions=['png'])
    return deco(lambda: zodiac.my_plot)()


def test_bar_png():
    deco = image_comparison(baseline_images=['bar'], remove_text=False, extensions=['png'])
    return deco(lambda: zodiac.my_bar)()


def test_hist_png():
    deco = image_comparison(baseline_images=['hist'], remove_text=False, extensions=['png'])
    return deco(lambda: zodiac.my_hist)()

