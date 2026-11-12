/*
 * Legacy response override has been intentionally disabled.
 * This script no longer changes API responses or fabricates Gold entitlements.
 * Keep this file only for compatibility with existing local proxy references.
 */
$done({ body: $response.body });
