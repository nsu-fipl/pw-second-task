from pathlib import Path
from matplotlib.testing.decorators import image_comparison
import zodiac



@image_comparison(
    baseline_images=["plot"],
    remove_text=False,
    extensions=["png"],
)
def test_plot_png():
    zodiac.my_plot()


@image_comparison(
    baseline_images=["bar"],
    remove_text=False,
    extensions=["png"],
)
def test_bar_png():
    zodiac.my_bar()


@image_comparison(
    baseline_images=["hist"],
    remove_text=False,
    extensions=["png"],
)
def test_hist_png():
    zodiac.my_hist()
