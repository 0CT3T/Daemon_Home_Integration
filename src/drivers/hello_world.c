
/*  
 *  hello-1.c - The simplest kernel module.
 */
#include <linux/module.h>	/* Needed by all modules */
#include <linux/kernel.h>	/* Needed for KERN_INFO */
#include <linux/init.h>
#define DRIVER_AUTHOR "Sébastien Amrhein <sebastien@amrhein.be>"
#define DRIVER_DESC   "A sample driver"

static int data __initdata = 3;

static int __init init_hello_world(void)
{
	printk(KERN_INFO "Hello world %d\n",data);

	/* 
	 * A non 0 return means init_module failed; module can't be loaded. 
	 */
	return 0;
}

static void __exit cleanup_hello_world(void)
{
	printk(KERN_INFO "Goodbye world 1.\n");
}


module_init(init_hello_world);
module_exit(cleanup_hello_world);

MODULE_LICENSE("MIT");

MODULE_AUTHOR(DRIVER_AUTHOR);	/* Who wrote this module? */
MODULE_DESCRIPTION(DRIVER_DESC);	/* What does this module do */
