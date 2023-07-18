# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
import cv2

class Real_time_monitoringPlugin(octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.StartupPlugin,
    octoprint.plugin.EventHandlerPlugin
):

    def get_settings_defaults(self):
        return {
            # put your plugin's default settings here
        }


    def get_assets(self):
        # Define your plugin's asset files to automatically include in the
        # core UI here.
        return {
            "js": ["js/real_time_monitoring.js"],
            "css": ["css/real_time_monitoring.css"],
            "less": ["less/real_time_monitoring.less"]
        }


    def get_update_information(self):
        # Define the configuration for your plugin to use with the Software Update
        # Plugin here. See https://docs.octoprint.org/en/master/bundledplugins/softwareupdate.html
        # for details.
        return {
            "real_time_monitoring": {
                "displayName": "Real_time_monitoring Plugin",
                "displayVersion": self._plugin_version,

                # version check: github repository
                "type": "github_release",
                "user": "you",
                "repo": "OctoPrint-Real_time_monitoring",
                "current": self._plugin_version,

                # update method: pip
                "pip": "https://github.com/you/OctoPrint-Real_time_monitoring/archive/{target_version}.zip",
            }
        }

    def on_event(self, event, payload):
        if event == "PrintStarted":
            self._logger.info("PrintStarted event received: %s \n\n\n\n\n\n\n" % str(payload))
            cv2.imshow("image", cv2.imread("printer.jpg"))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        if event == "ZChange":
            self._logger.info("ZChange event received: %s" % str(payload))
        return super().on_event(event, payload)




__plugin_name__ = "Real_time_monitoring Plugin"
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = Real_time_monitoringPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
