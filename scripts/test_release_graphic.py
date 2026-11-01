import unittest

from release_graphic import INK, rendered_icon


class ReleaseGraphicTest(unittest.TestCase):
    def test_sun_has_a_complete_circle_and_eight_rays(self):
        image = rendered_icon("sun", size=240, stroke=INK)
        alpha = image.getchannel("A")
        for x, y in [(12, 2), (12, 22), (2, 12), (22, 12),
                     (5, 5), (19, 5), (5, 19), (19, 19),
                     (12, 7), (17, 12), (12, 17), (7, 12)]:
            with self.subTest(x=x, y=y):
                self.assertGreater(alpha.getpixel((x * 10, y * 10)), 0)
        self.assertEqual(alpha.getpixel((120, 120)), 0)
        left, top, right, bottom = alpha.getbbox()
        self.assertGreater(min(left, top), 0)
        self.assertLess(max(right, bottom), 240)


if __name__ == "__main__":
    unittest.main()
