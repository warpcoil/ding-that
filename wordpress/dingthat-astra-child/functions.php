<?php
/**
 * Ding That: Astra child theme.
 *
 * @package Ding_That
 */

defined( 'ABSPATH' ) || exit;

define( 'DINGTHAT_CHILD_VERSION', '1.0.0' );

/**
 * Address visitors use to download the Ding That fonts.
 * Set it in Appearance › Customize › Ding That, or with the `dingthat_download_url` filter.
 *
 * @return string
 */
function dingthat_download_url() {
	$url = get_theme_mod( 'dingthat_download_url', 'https://github.com/warpcoil/ding-that/releases/latest' );
	return (string) apply_filters( 'dingthat_download_url', $url );
}

/**
 * Address of the source code repository.
 *
 * @return string
 */
function dingthat_repo_url() {
	$url = get_theme_mod( 'dingthat_repo_url', 'https://github.com/warpcoil/ding-that' );
	return (string) apply_filters( 'dingthat_repo_url', $url );
}

/**
 * Styles: the child stylesheet loads after Astra's, so its tokens win.
 */
function dingthat_enqueue_styles() {
	wp_enqueue_style(
		'dingthat-child',
		get_stylesheet_uri(),
		array( 'astra-theme-css' ),
		DINGTHAT_CHILD_VERSION
	);

	// The theme self-hosts its fonts. If a Google font was ever chosen in the
	// Customizer, stop Astra requesting it, so no visitor data goes to Google.
	wp_dequeue_style( 'astra-google-fonts' );
}
add_action( 'wp_enqueue_scripts', 'dingthat_enqueue_styles', 20 );

/**
 * Preload the body font and the Objects font (used in the hero) so they render straight away.
 */
function dingthat_preload_fonts() {
	$fonts = array( 'AtkinsonHyperlegibleNext-Variable.woff2', 'DingThatObjects-Regular.woff2' );
	foreach ( $fonts as $font ) {
		printf(
			'<link rel="preload" href="%s" as="font" type="font/woff2" crossorigin>' . "\n",
			esc_url( get_stylesheet_directory_uri() . '/fonts/' . $font )
		);
	}
}
add_action( 'wp_head', 'dingthat_preload_fonts', 1 );

/**
 * Theme supports: make the block editor look like the front end.
 */
function dingthat_setup() {
	load_child_theme_textdomain( 'dingthat', get_stylesheet_directory() . '/languages' );
	add_theme_support( 'editor-styles' );
	add_editor_style( 'style.css' );
}
add_action( 'after_setup_theme', 'dingthat_setup', 20 );

/**
 * Pattern category and block styles.
 * Patterns themselves are loaded automatically from the /patterns folder.
 */
function dingthat_register_blocks() {
	register_block_pattern_category(
		'dingthat',
		array( 'label' => __( 'Ding That', 'dingthat' ) )
	);

	register_block_style(
		'core/group',
		array(
			'name'  => 'dt-notice',
			'label' => __( 'Notice', 'dingthat' ),
		)
	);
	register_block_style(
		'core/list',
		array(
			'name'  => 'dt-toc',
			'label' => __( 'Contents', 'dingthat' ),
		)
	);
	register_block_style(
		'core/paragraph',
		array(
			'name'  => 'dt-eyebrow',
			'label' => __( 'Eyebrow label', 'dingthat' ),
		)
	);
}
add_action( 'init', 'dingthat_register_blocks' );

/**
 * [ding] shortcode: show a Ding That glyph anywhere a shortcode works.
 *
 * Examples:
 *   [ding font="objects" key="h"]                  decorative house, hidden from screen readers
 *   [ding font="shapes" key="v" label="Done"]      a check that screen readers announce as "Done"
 *
 * @param array $atts Shortcode attributes: font (gui, shapes or objects), key, label.
 * @return string
 */
function dingthat_ding_shortcode( $atts ) {
	$atts = shortcode_atts(
		array(
			'font'  => 'objects',
			'key'   => '',
			'label' => '',
		),
		$atts,
		'ding'
	);

	$font = in_array( $atts['font'], array( 'gui', 'shapes', 'objects' ), true ) ? $atts['font'] : 'objects';
	$key  = (string) $atts['key'];
	if ( '' === $key ) {
		return '';
	}

	$class = 'dt-g dt-g--' . $font . ' dt-ding';
	if ( '' === $atts['label'] ) {
		return sprintf( '<span class="%s" aria-hidden="true">%s</span>', esc_attr( $class ), esc_html( $key ) );
	}
	return sprintf(
		'<span class="%1$s" role="img" aria-label="%2$s"><span aria-hidden="true">%3$s</span></span>',
		esc_attr( $class ),
		esc_attr( $atts['label'] ),
		esc_html( $key )
	);
}
add_shortcode( 'ding', 'dingthat_ding_shortcode' );

/**
 * Customizer: where the downloads and the source code live.
 *
 * @param WP_Customize_Manager $wp_customize Customizer instance.
 */
function dingthat_customize_register( $wp_customize ) {
	$wp_customize->add_section(
		'dingthat',
		array(
			'title'       => __( 'Ding That', 'dingthat' ),
			'description' => __( 'Settings used by the Ding That block patterns.', 'dingthat' ),
			'priority'    => 30,
		)
	);
	$wp_customize->add_setting(
		'dingthat_download_url',
		array(
			'default'           => 'https://github.com/warpcoil/ding-that/releases/latest',
			'sanitize_callback' => 'esc_url_raw',
		)
	);
	$wp_customize->add_control(
		'dingthat_download_url',
		array(
			'label'       => __( 'Download address', 'dingthat' ),
			'description' => __( 'Where visitors download the fonts: a GitHub release, or a zip file in your media library. Used by the "Download the fonts" buttons in the patterns.', 'dingthat' ),
			'section'     => 'dingthat',
			'type'        => 'url',
		)
	);
	$wp_customize->add_setting(
		'dingthat_repo_url',
		array(
			'default'           => 'https://github.com/warpcoil/ding-that',
			'sanitize_callback' => 'esc_url_raw',
		)
	);
	$wp_customize->add_control(
		'dingthat_repo_url',
		array(
			'label'       => __( 'Source code address', 'dingthat' ),
			'description' => __( 'The GitHub repository for the fonts.', 'dingthat' ),
			'section'     => 'dingthat',
			'type'        => 'url',
		)
	);
}
add_action( 'customize_register', 'dingthat_customize_register' );

/**
 * Type tester scripts. Registered here, and loaded only on pages that use [ding_tester].
 */
function dingthat_register_tester_assets() {
	$uri = get_stylesheet_directory_uri() . '/assets/js/';
	wp_register_script( 'dingthat-glyph-data', $uri . 'glyph-data.js', array(), DINGTHAT_CHILD_VERSION, true );
	wp_register_script( 'dingthat-type-tester', $uri . 'type-tester.js', array( 'dingthat-glyph-data' ), DINGTHAT_CHILD_VERSION, true );
}
add_action( 'wp_enqueue_scripts', 'dingthat_register_tester_assets' );

/**
 * [ding_tester] shortcode: the interactive type tester and glyph picker.
 *
 * Example: [ding_tester font="objects"]   (font: gui, shapes or objects; the tab that opens first)
 *
 * @param array $atts Shortcode attributes.
 * @return string
 */
function dingthat_tester_shortcode( $atts ) {
	static $count = 0;
	++$count;
	$atts = shortcode_atts( array( 'font' => 'gui' ), $atts, 'ding_tester' );
	$font = in_array( $atts['font'], array( 'gui', 'shapes', 'objects' ), true ) ? $atts['font'] : 'gui';
	$id   = 'dt-tester-' . $count;

	wp_enqueue_script( 'dingthat-type-tester' );

	$tabs = '';
	foreach ( array( 'gui' => 'GUI', 'shapes' => 'Shapes', 'objects' => 'Objects' ) as $key => $label ) {
		$tabs .= sprintf(
			'<button type="button" role="tab" id="%1$s-tab-%2$s" aria-controls="%1$s-panel" aria-selected="%3$s" data-dt-font="%2$s">%4$s</button>',
			esc_attr( $id ),
			esc_attr( $key ),
			$key === $font ? 'true' : 'false',
			esc_html( $label )
		);
	}

	ob_start();
	?>
	<div class="dt-tester" id="<?php echo esc_attr( $id ); ?>" data-font="<?php echo esc_attr( $font ); ?>">
		<div class="dt-tester-tabs" role="tablist" aria-label="<?php esc_attr_e( 'Choose a font', 'dingthat' ); ?>"><?php echo $tabs; // phpcs:ignore WordPress.Security.EscapeOutput -- escaped above. ?></div>
		<div class="dt-tester-panel" id="<?php echo esc_attr( $id ); ?>-panel" role="tabpanel">
			<div class="dt-tester-head">
				<h2 class="dt-tester-family"><?php echo esc_html( 'Ding That ' . ucfirst( 'gui' === $font ? 'GUI' : $font ) ); ?></h2>
				<span class="dt-tester-count"></span>
			</div>
			<div class="dt-tester-controls">
				<label for="<?php echo esc_attr( $id ); ?>-text"><?php esc_html_e( 'Text to preview', 'dingthat' ); ?></label>
				<textarea id="<?php echo esc_attr( $id ); ?>-text" class="dt-tester-text" rows="3" spellcheck="false" autocapitalize="off" autocomplete="off"></textarea>
				<div class="dt-tester-row">
					<label for="<?php echo esc_attr( $id ); ?>-size"><?php esc_html_e( 'Size', 'dingthat' ); ?></label>
					<input type="range" id="<?php echo esc_attr( $id ); ?>-size" class="dt-tester-size" min="16" max="120" value="56">
					<output class="dt-tester-size-value" for="<?php echo esc_attr( $id ); ?>-size">56 px</output>
					<button type="button" class="dt-tester-reset"><?php esc_html_e( 'Reset sample', 'dingthat' ); ?></button>
				</div>
			</div>
			<p class="screen-reader-text"><?php esc_html_e( 'The preview below shows the text above in the chosen picture font. Screen readers read the letters in the text box.', 'dingthat' ); ?></p>
			<div class="dt-tester-output" aria-hidden="true"></div>
			<h3 class="dt-tester-grid-title"><?php esc_html_e( 'Every glyph', 'dingthat' ); ?></h3>
			<p class="dt-tester-hint"><?php esc_html_e( 'Choose a glyph to add it to the preview. In browsers that allow it, the character is also copied, ready to paste.', 'dingthat' ); ?></p>
			<div class="dt-tester-grid"></div>
			<p class="dt-tester-status screen-reader-text" role="status" aria-live="polite"></p>
		</div>
		<noscript><p><?php esc_html_e( 'The type tester needs JavaScript. The Fonts page lists every glyph and its key.', 'dingthat' ); ?> <a href="/fonts/"><?php esc_html_e( 'See the character maps', 'dingthat' ); ?></a></p></noscript>
	</div>
	<?php
	return (string) ob_get_clean();
}
add_shortcode( 'ding_tester', 'dingthat_tester_shortcode' );
