<?php
/**
 * Title: Licence and open source (dark band)
 * Slug: dingthat/dark-band
 * Categories: dingthat
 * Description: Two columns on a dark band: the free licence and the open source.
 * Viewport Width: 1400
 *
 * @package Ding_That
 */

defined( 'ABSPATH' ) || exit;
?>
<!-- wp:group {"align":"full","tagName":"section","className":"dt-band dt-band--dark","layout":{"type":"default"}} -->
<section class="wp-block-group alignfull dt-band dt-band--dark"><!-- wp:group {"className":"dt-wrap","layout":{"type":"default"}} -->
<div class="wp-block-group dt-wrap"><!-- wp:columns -->
<div class="wp-block-columns"><!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading -->
<h2 class="wp-block-heading">Free for any project</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>The Ding That fonts are released under the SIL Open Font License 1.1. Use the fonts in documents, apps, games, logos and websites, and bundle them with your own software. The one thing you can’t do is sell the fonts on their own.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p><a href="/open-source/">Read about the licence</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
<!-- wp:column -->
<div class="wp-block-column"><!-- wp:heading -->
<h2 class="wp-block-heading">Open source</h2>
<!-- /wp:heading -->
<!-- wp:paragraph -->
<p>Every glyph is drawn by a short Python script, and the same script builds all the font files. Read it, suggest new glyphs or report a problem on GitHub.</p>
<!-- /wp:paragraph -->
<!-- wp:paragraph -->
<p><a href="<?php echo esc_url( dingthat_repo_url() ); ?>">View the source on GitHub</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:column -->
</div>
<!-- /wp:columns -->
</div>
<!-- /wp:group -->
</section>
<!-- /wp:group -->
