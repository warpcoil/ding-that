<?php
/**
 * Title: Type tester
 * Slug: dingthat/type-tester
 * Categories: dingthat
 * Description: The interactive type tester and glyph picker, on a plain band.
 * Viewport Width: 1400
 *
 * @package Ding_That
 */

defined( 'ABSPATH' ) || exit;
?>
<!-- wp:group {"align":"full","tagName":"section","className":"dt-band","layout":{"type":"default"}} -->
<section class="wp-block-group alignfull dt-band"><!-- wp:group {"className":"dt-wrap","layout":{"type":"default"}} -->
<div class="wp-block-group dt-wrap"><!-- wp:group {"className":"dt-intro","layout":{"type":"default"}} -->
<div class="wp-block-group dt-intro"><!-- wp:heading -->
<h2 class="wp-block-heading">Try the fonts</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Type in the box, or choose glyphs from the grid, to see them in each font.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
<!-- wp:shortcode -->
[ding_tester font="objects"]
<!-- /wp:shortcode -->
</div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
