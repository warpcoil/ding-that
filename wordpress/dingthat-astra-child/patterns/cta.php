<?php
/**
 * Title: Call to action box
 * Slug: dingthat/cta
 * Categories: dingthat
 * Description: Bordered box with a heading, a tip and two buttons.
 * Viewport Width: 1400
 *
 * @package Ding_That
 */

defined( 'ABSPATH' ) || exit;
?>
<!-- wp:group {"align":"full","tagName":"section","className":"dt-band","layout":{"type":"default"}} -->
<section class="wp-block-group alignfull dt-band"><!-- wp:group {"className":"dt-wrap","layout":{"type":"default"}} -->
<div class="wp-block-group dt-wrap"><!-- wp:group {"className":"dt-cta","layout":{"type":"default"}} -->
<div class="wp-block-group dt-cta"><!-- wp:group {"layout":{"type":"default"}} -->
<div class="wp-block-group"><!-- wp:heading -->
<h2 class="wp-block-heading">Ready to type?</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>After installing, restart your apps so they find the new fonts. On a website, hide decorative glyphs from screen readers with <code>aria-hidden="true"</code>, and give meaningful ones a text label.</p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->
<!-- wp:buttons -->
<div class="wp-block-buttons"><!-- wp:button -->
<div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="<?php echo esc_url( dingthat_download_url() ); ?>">Download the fonts</a></div>
<!-- /wp:button -->
<!-- wp:button {"className":"is-style-outline"} -->
<div class="wp-block-button is-style-outline"><a class="wp-block-button__link wp-element-button" href="/faq/">Read the FAQ</a></div>
<!-- /wp:button -->
</div>
<!-- /wp:buttons -->
</div>
<!-- /wp:group -->
</div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
