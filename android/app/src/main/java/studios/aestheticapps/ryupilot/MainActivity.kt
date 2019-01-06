package studios.aestheticapps.ryupilot

import android.os.Bundle
import android.support.v7.app.AlertDialog
import android.support.v7.app.AppCompatActivity
import android.view.LayoutInflater
import android.view.ViewGroup
import android.widget.EditText
import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.content_main.*

class MainActivity : AppCompatActivity()
{
    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)

        createIpAddressPanel()
        createSettingsPanel()
    }

    private fun createIpAddressPanel()
    {
        ipAddressTv.text = PrefsHelper.obtainRyuIpAddress(this)
        setIpAddressBtn.setOnClickListener { showIpInputDialog() }
    }

    private fun createSettingsPanel()
    {
        val settings = arrayListOf(ID_SETTING_1, ID_SETTING_2, ID_SETTING_3, ID_SETTING_4)
        val buttons = arrayListOf(setting1Btn, setting2Btn, setting3Btn, setting4Btn)

        var i = 0
        buttons.forEach { button ->
            button.setOnClickListener {
                // send http request with parameter settings[i]
                i++
            }
        }

        setIpAddressBtn.setOnClickListener { showIpInputDialog() }
    }

    private fun showIpInputDialog()
    {
        val builder = AlertDialog.Builder(this)
        val viewInflated = LayoutInflater
            .from(this)
            .inflate(
                R.layout.ip_input_dialog,
                cardView as ViewGroup,
                false
            )

        val inputIpTextLayout = viewInflated.findViewById(R.id.inputIpTextLayout) as EditText
        builder.apply {
            setTitle(getString(R.string.set_ryu_controller_ip))
            setView(viewInflated)
            setNegativeButton(android.R.string.cancel) { dialog, _ -> dialog.cancel() }
            setPositiveButton(android.R.string.ok) { dialog, _ ->
                val newAddress = inputIpTextLayout.text.toString()
                PrefsHelper.setRyuIpAddress(context, newAddress)
                ipAddressTv.text = newAddress
                dialog.dismiss()
            }

            show()
        }
    }

    private companion object
    {
        const val ID_SETTING_1 = "1"
        const val ID_SETTING_2 = "2"
        const val ID_SETTING_3 = "3"
        const val ID_SETTING_4 = "4"
    }
}
